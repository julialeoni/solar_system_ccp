'''
Simulação do sistema solar
inclui os planetas e o cometa Halley
'''

import numpy as np
import datetime as dt
import vpython as vp
import ephem
import cometas

# sun at the center
sun = vp.sphere(pos=vp.vector(0, 0, 0), radius=0.1, texture='images/sun.jpg')

# creating the list of objects to be followed
objects = [ephem.Mercury(), ephem.Venus(), ephem.Sun(), ephem.Mars(), ephem.Jupiter(), ephem.Saturn(), ephem.Uranus(), ephem.Neptune(), cometas.create_halley(), cometas.create_ztf()]

N = len(objects)
now = dt.datetime.now()

''' Determines the position of the object at date
    Converts from ecliptic (spherical) to cartesian coordinates
    The xy plane will be the plane of the ecliptic, with the x axis pointing to the vernal equinox '''
def locate(obj, date, earth=False):

    obj.compute(date)  # using ephem.compute() method to get object coordinates
    th, ph = obj.hlat, obj.hlon

    # earth must be treated separatelly
    if obj.name == 'Sun':  # the Earth
        r = obj.earth_distance
    else:
        r = obj.sun_distance

    # converting to cartesian coordinates
    x = r * np.cos(ph) * np.cos(th)
    y = r * np.sin(ph) * np.cos(th)
    z = r * np.sin(th)
    return x, y, z

# texture generator
# Returns (with yield) elements from textures. After len(textures) calls, wraps and starts again from the beginning
textures = ['images/mercury.png', 'images/venus.jpg', vp.textures.earth, 'images/mars.jpg', 'images/jupiter.png', 'images/saturn.jpg', 'images/uranus.png', 'images/neptune.jpg', 'images/comet']
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
    balls.append(vp.sphere(pos=pos, radius=0.075, texture=next(texture)))
    tr = vp.curve(pos)
    tr.radius = 0.005
    tr.retain = 10 * 365  # will retain only the last tr.retain positions
    tracks.append(tr)

# animation function
n = 1
while True:
    vp.rate(365)
    date = now + dt.timedelta(days=n)  # increasing date day by day
    for (p, b, t) in zip(objects, balls, tracks):  # relocating objects
        x, y, z = locate(p, date)
        b.pos = vp.vector(x, y, z)
        t.append(b.pos)
    n += 1



