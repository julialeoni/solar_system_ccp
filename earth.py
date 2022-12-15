'''
Simulação da Terra com satélites artificiais (Amazônia-1, ISS, CBERS-4 e Hubble) e natural (Lua)
'''

import numpy as np
import datetime as dt
import vpython as vp
import ephem
import satelites

# Terra no centro
earth = vp.sphere(pos=vp.vector(0, 0, 0), radius= ephem.earth_radius/1.496e+11, texture= vp.textures.earth)

# creating the list of objects to be followed

objects = [ephem.Moon(), satelites.amazonia1, satelites.iss, satelites.cbers4, satelites.hst]

N = len(objects)
now = dt.datetime.now()

''' Determines the position of the object at date
    Converts from ecliptic (spherical) to cartesian coordinates
'''

def locate(obj, date):
    obj.compute(date)  # using ephem.compute() method to get object coordinates
    if obj.name != 'Moon':
        th, ph = obj.sublat, obj.sublong
        r = (obj.elevation + ephem.earth_radius)/1.496e+11
    else:
        th, ph = obj.hlat, obj.hlon
        r = obj.earth_distance
    # converting to cartesian coordinates
    x = r * np.cos(ph) * np.cos(th)
    y = r * np.sin(ph) * np.cos(th)
    z = r * np.sin(th)
    return x, y, z

# texture generator
# Returns (with yield) elements from textures. After len(textures) calls, wraps and starts again from the beginning
textures = ['images/moon.jpg', vp.color.green, vp.color.white, vp.color.red, vp.color.blue]
def pick_texture():
    n = 0
    while True:
        yield textures[n]
        n = (n + 1) % len(textures)
texture = pick_texture()

# creating the scene with vpython
vp.scene.width = 1500
vp.scene.height = 700
vp.scene.background = vp.color.black

# creating animated objects
balls = []  # position of objects
tracks = []  # trace of the object's orbit
for (p, i) in zip(objects, range(N)):
    x, y, z = locate(p, now)
    pos = vp.vector(x, y, z)
    print(p.name)
    if p.name == 'Moon':
        balls.append(vp.sphere(pos=pos, radius=(ephem.earth_radius / 1.496e+11)/2, texture=next(texture)))
    else:
        balls.append(vp.sphere(pos=pos, radius=(ephem.earth_radius / 1.496e+11)/10, color=next(texture)))
    tr = vp.curve(pos)
    tr.radius = (ephem.earth_radius/1.496e+11)/100
    if p.name == 'Moon':
        tr.retain = 500  # will retain only the last tr.retain positions
    else:
        tr.retain = 60
    tracks.append(tr)

# animation function
n = 0
while True:
    vp.rate(100)
    date = now + dt.timedelta(minutes=n)  # increasing date minute by minute
    for (p, b, t) in zip(objects, balls, tracks):  # relocating objects
        x, y, z = locate(p, date)
        b.pos = vp.vector(x, y, z)
        t.append(b.pos)
    n += 1