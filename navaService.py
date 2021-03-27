class ServiceNava:
    def __init__(self, repository, validator):
        """
        desc:initializeaza clasa Service1
        :param repository:
        """
        self.__repo = repository
        self.__valid = validator

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
