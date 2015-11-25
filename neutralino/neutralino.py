import .consts as consts


class Neutralino:
    def __init__(self):
        self._vars = {}

    def addVariable(self, title, value):
        ''' addVariable needs for finding results with this variables
        '''
        self._vars[title] = value

    def newtonLaw(self, M1, M2, r):
        if r <= 0:
            raise Exception("Radius must be a positive number")
        return (consts.G * M1 * M2)/r

    def gravity_acc(self, Mcentral, dist):
        if dist <= 0:
            raise Exception("Distance must be a positive number")
        return consts.G * Mcentral/dist**2

    def period(self, R, v):
        if v <= 0:
            raise Exception("Velocity must be a positive number")
        return 2 * consts.PI * R/v
