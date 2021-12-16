import time

class Timer:
    startTime = None
    lapStartTime = None

    def Start(self):
        self.startTime = time.time()
        self.lapStartTime = self.startTime
        return time.asctime(time.localtime(self.startTime))


    def Stop(self):
        tempStartTime = self.startTime
        self.startTime = None
        self.lapStartTime = None
        return f"{time.time() - tempStartTime:.3f}"


    def Reset(self):
        self.startTime = time.time()
        self.lapStartTime = self.startTime
        return time.asctime(time.localtime(self.startTime))


    def Lap(self):
        deltaTime = time.time() - self.lapStartTime
        self.lapStartTime = self.lapStartTime + deltaTime
        return f"{deltaTime:.3f}"