from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15
    TYPE = 'Secondary'

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self):
        return super().details()


