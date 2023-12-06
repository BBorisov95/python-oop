from typing import List
from project.band_members.musician import Musician


class Band:

    SINGERS = 0
    DRUMMERS = 0
    GUITARISTS = 0

    def __init__(self, name: str):
        self.name = name
        self.members: List[Musician] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Band name should contain at least one character!')
        self.__name = value

    def increment_musician_type(self, musician):
        if musician.__class__.__name__ == "Guitarist":
            self.GUITARISTS += 1
        elif musician.__class__.__name__ == "Drummer":
            self.DRUMMERS += 1
        elif musician.__class__.__name__ == "Singer":
            self.SINGERS += 1

    def __str__(self):
        return f'{self.name} with {len(self.members)} members.'
