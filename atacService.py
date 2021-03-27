from Domain.NaveSpatiale import *


class ServiceAtac:
    def __init__(self, repository, validator, repoNava):
        """
        desc:initializeaza clasa Service1
        :param repository:
        """
        self.__repo = repository
        self.__valid = validator
        self.__repoNava = repoNava

    def create1(self, obj):
        """

        :param obj:
        :return:
        """
        self.__valid.validate(obj)
        self.__repo.create(obj)

    def update1(self, obj):
        c = self.__repo.read(obj.getId())
        self.__repo.update(obj)

    def delete1(self, id_obj):
        clients = self.__repo.read()
        for client in clients:
            if client.getId() == id_obj:
                self.__repo.delete(id_obj)
                return

    def read1(self, obj_id=None):
        return self.__repo.read(obj_id)

    def atac(self, theId):
        nave = self.__repoNava.read()
        if self.__repo.read(theId) is None:
            raise ValueError("Nu exista aceast atac")
        atacata = self.__repo.read(theId).getIdNavaAtacata()
        pagube = int(self.__repo.read(theId).getPagube())
        for n in nave:
            if n.getId() == atacata:
                points = str(int(n.getCurentHitPoints()) - pagube)
                if int(points) < 0:
                    points = '0'
                theId = n.getId()
                tip = n.getTip()
                maxHitPoints = n.getMaxHitPoints()
                entity = Nave(theId, tip, maxHitPoints, points)
                self.__repoNava.update(entity)
                break

    def __dictionarSumaPagube(self):
        nave = self.__repoNava.read()
        atacuri = self.__repo.read()
        dict = {}
        for n in nave:
            pagube = 0
            for a in atacuri:
                if a.getIdNavaAtacator() == n.getId():
                    pagube += int(a.getPagube())
            dict[n.getId()] = pagube
        return dict

    def ordonare(self):
        dict = self.__dictionarSumaPagube()
        nave = self.__repoNava.read()
        return sorted(nave, key=lambda nav: dict[nav.getId()], reverse=True)

    def bataliiNava(self, nava):
        atacuri = self.__repo.read()
        listaBatalii = []
        for a in atacuri:
            if a.getIdNavaAtacator() == nava.getId() or a.getIdNavaAtacata() == nava.getId():
                listaBatalii.append(a)
        return listaBatalii

    def batalii(self):
        nave = self.__repoNava.read()
        countAtacuri = 0
        countBatalii = 0
        for i in range(len(nave)):
            batalii = self.bataliiNava(nave[i])
            for j in range(i + 1, len(nave)):
                idNava2 = nave[j].getId()
                bataliiComune = []
                countAtacuri = 0
                for b in batalii:
                    if b.getIdNavaAtacator() == idNava2 or b.getIdNavaAtacata() == idNava2:
                        countAtacuri += 1
                        bataliiComune.append(b)
                if countAtacuri > 0:
                    countBatalii += 1
                    print("Batalia ", countBatalii, " : ")
                    for i in range(countAtacuri):
                        print("Atacul ", i+1, " : ", bataliiComune[i])
                    print()

