'''
Simulação do sistema de Jupiter
'''

import datetime as dt
import vpython as vp
import ephem

#criando a lista de objetos

jraio = 69911000/1.496e+11 # raio de jupiter em unidades astronomicas

Jupiter = vp.sphere(pos=vp.vector(0, 0, 0), radius= jraio, texture= 'images/jupiter.png')
objects = [ephem.Io(), ephem.Ganymede(), ephem.Callisto(), ephem.Europa()]

N = len(objects)  # no. of objects
now = dt.datetime.now()

def locate(obj, date):
    '''
        returns the x, y, z coordinates relative to Jupiter in terms of planet radius
    '''
    obj.compute(date)  # using ephem .compute() method to get object coordinates
    x, y, z = obj.x*jraio, obj.y*jraio, obj.z*jraio
    return x, y, z

# ******************************************
# texture generator
# Returns (with yield) elements from colors. After len(textures) calls, wraps and starts again from the beginning
colors = [vp.color.green, vp.color.white, vp.color.red, vp.color.blue, vp.color.cyan]
def pick_color():
    n = 0
    while True:
        yield colors[n]
        n = (n + 1) % len(colors)
texture = pick_color()
# ******************************************

#criando a cena em vpython
vp.scene.width = vp.scene.height = 500
vp.scene.background = vp.color.black

#creating animated objects
balls = []  # position of objects
tracks = []  # trace of the object's orbit
for (p, i) in zip(objects, range(N)):
    x, y, z = locate(p, now)
    pos = vp.vector(x, y, z)
    balls.append(vp.sphere(pos=pos, radius=jraio/5, color=next(texture)))
    tr = vp.curve(pos)
    tr.radius = jraio/30
    tr.retain = 40  # will retain only the last tr.retain positions
    tracks.append(tr)

# animation function
n = 1
while True:
    vp.rate(100)
    date = now + dt.timedelta(hours=n)  # increasing date hour by hour
    for (p, b, t) in zip(objects, balls, tracks):  # relocating objects
        x, y, z = locate(p, date)
        b.pos = vp.vector(x, y, z)
        t.append(b.pos)
    n += 1