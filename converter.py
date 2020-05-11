import math


class Converter:
    def rectangular2spherical(x, y, z, xhat, yhat, zhat):
        r = ((x ** 2) + (y ** 2) + (z ** 2)) ** (1 / 2)
        omega = math.acos(z / r)
        phi = math.atan2(y, x)
        fr = (xhat * math.sin(omega) * math.cos(phi)) + (yhat * math.sin(omega) * math.sin(phi)) + \
             (zhat * math.cos(omega))
        fomega = (xhat * math.cos(omega) * math.cos(phi)) + (yhat * math.cos(omega) * math.sin(phi)) - \
                 (zhat * math.sin(omega))
        fphi = (xhat * math.sin(phi) * -1) + (yhat * math.cos(phi))
        omega = math.degrees(omega)
        phi = math.degrees(phi)
        spherical = [r, omega, phi, fr, fomega, fphi]
        return spherical

    print(rectangular2spherical(3, 4, 12, 9, 8, 36))
