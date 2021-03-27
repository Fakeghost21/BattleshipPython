from Domain.entity import *


class Nave(Entity):
    def __init__(self, theId, tip, maxHitPoints, curentHitPoints):
        super().__init__(theId)
        self.__tip = tip
        self.__maxHitPoints = maxHitPoints
        self.__curentHitPoints = curentHitPoints

    def getTip(self):
        return self.__tip

    def getMaxHitPoints(self):
        return self.__maxHitPoints

    def getCurentHitPoints(self):
        return self.__curentHitPoints

    def setCurentHitPoints(self, points):
        self.__curentHitPoints = points

    def __str__(self):
        return "{},{},{},{}".format(
            self.getId(),
            self.__tip,
            self.__maxHitPoints,
            self.__curentHitPoints
        )


