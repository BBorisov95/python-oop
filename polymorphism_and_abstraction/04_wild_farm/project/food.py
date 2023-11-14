from abc import abstractmethod, ABC


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __repr__(self):
        return f'{self.__class__.__name__}'

class Vegetable(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Fruit(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Meat(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Seed(Food):
    def __init__(self, quantity: int):
        super().__init__(quantity)

    def __repr__(self):
        return f'{self.__class__.__name__}'
