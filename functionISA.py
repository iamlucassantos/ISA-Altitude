def calculator(altitudeinput):
    from math import exp
    import numpy as np

    def isa(pressure,temperature,walk,a):
        R = 287  # [J/kgK]
        g0 = 9.80665  # [m/s2]

        temperatureend = temperature + a*walk
        if a ==0:
            pressureend = pressure * exp(g0 * walk / (-R * temperatureend))
        else:
            pressureend = pressure * (temperatureend / temperature)**(-g0 / (a * R))
        densityend = pressureend / (R * temperatureend)

        return (temperatureend,pressureend,densityend)

    def atmosjump(p1,t1,alt):
        altitudes = np.array([11000, 20000, 32000, 47000, 51000, 71000])
        allA = np.array([-0.0065,0,0.001,0.0028,0,-0.0028,-0.002])
        idx = len(altitudes[altitudes<alt]) + 1

        for i in range(idx):
            p0 = p1
            t0 = t1
            h1 = min(alt,altitudes[i])
            if i>0:
                h1 = h1-altitudes[i-1]
            a = allA[i]
            t1, p1, rho1 = isa(p0, t0, h1, a)

        return (t1,p1,rho1)

    t1,p1,dens= atmosjump(101325.0 ,288.15, altitudeinput)

    print(t1,p1,dens)
    return(t1,p1,dens)

