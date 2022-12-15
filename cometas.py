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

def create_ztf():   #https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1003845
    ztf = ephem.HyperbolicBody()
    ztf_epoch = '2022-07-29'
    ztf_epoch_p = '2023-02-01'
    ztf._inc = 109.17
    ztf._Om = 302.5537
    ztf._om = 145.8149
    ztf._e = 1.000267
    ztf._q = 1.112253
    ztf.name = 'C/2022 E3 ZTF'
    return ztf

'''_HyperbolicBody elements:
_epoch — Equinox year for _inc, _Om, and _om
_epoch_p — Epoch of perihelion
_inc — Inclination (°)
_Om — Longitude of ascending node (°)
_om — Argument of perihelion (°)
_e — Eccentricity
_q — Perihelion distance (AU)
_g, _k — Magnitude model coefficients
_size — Angular size in arcseconds at 1 AU'''