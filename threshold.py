class threshold:



    def __init__(self,hHigh,hLow,sHigh,sLow,vHigh,vLow):
        self.hmin = hLow
        self.hmax = hHigh
        self.smin = sLow
        self.smax = sHigh
        self.vmin = vLow
        self.vmax = vHigh

    def getHMax(self):
        return self.hmax

    def getHMin(self):
        return self.hmin

    def getSMax(self):
        return self.smax

    def getSMin(self):
        return self.smin

    def getVMax(self):
        return self.vmax

    def getVMin(self):
        return self.vmin

    def setHMax(self,val):
        self.hmax = val

    def setHMin(self,val):
        self.hmin = val

    def setSMax(self,val):
        self.smax = val

    def setSMin(self,val):
        self.smin = val

    def setVMax(self,val):
        self.vmax = val

    def setVMin(self,val):
        self.vmin = val

currentThresh = threshold(24, 6, 207, 88, 255, 100)
