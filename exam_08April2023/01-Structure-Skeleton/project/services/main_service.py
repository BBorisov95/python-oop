from project.services.base_service import BaseService


class MainService(BaseService):

    CAPACITY = 30
    TYPE = 'Main'

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        return super().details()


