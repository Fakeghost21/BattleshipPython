from Domain.entity import *


class Atac(Entity):
    def __init__(self, theId, idNavaAtacator, idNavaAtacata, pagube):
        super().__init__(theId)
        self.__idNavaAtacator = idNavaAtacator
        self.__idNavaAtacata = idNavaAtacata
        self.__pagube = pagube

    def getIdNavaAtacator(self):
        return self.__idNavaAtacator

    def getIdNavaAtacata(self):
        return self.__idNavaAtacata

    def getPagube(self):
        return self.__pagube

    def __str__(self):
        return "{},{},{},{}".format(
            self.getId(),
            self.__idNavaAtacator,
            self.__idNavaAtacata,
            self.__pagube
        )