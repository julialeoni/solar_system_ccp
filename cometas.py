import ephem

'''
EllipticalBody elements:
_inc — Inclination (°)
_Om — Longitude of ascending node (°)
_om — Argument of perihelion (°)
_a — Mean distance from sun (AU)
_M — Mean anomaly from the perihelion (°)
_epoch_M — Date for measurement _M
_size — Angular size (arcseconds at 1 AU)
_e — Eccentricity
_epoch — Epoch for _inc, _Om, and _om
_H, _G — Parameters for the H/G magnitude model
_g, _k — Parameters for the g/k magnitude model
'''

def create_halley():
    halley = ephem.EllipticalBody()
    halley._inc = 161.96
    halley._Om = 59.396
    halley._om = 112.05
    halley._a = 17.866
    halley._M = 0.07323
    halley._e = 0.96658
    halley_epoch_M = '2061-08-04'
    halley_epoch = '2061-08-04'
    halley.name = 'Halley'
    return halley

   
