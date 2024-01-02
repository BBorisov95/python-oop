from abc import ABC, abstractmethod
from typing import List
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    TIME_TO_REDUCE: float
    DIVER_OXYGEN_LEVEL: float

    def __init__(self, name: str, oxygen_level: float):
        self.name: str = name
        self.oxygen_level: float = oxygen_level
        self.catch: List[BaseFish] = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    @property
    def competition_points(self):
        return float(round(self.__competition_points, 1))

    @competition_points.setter
    def competition_points(self, value):
        self.__competition_points = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Diver name cannot be null or empty!')
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError('Cannot create diver with negative oxygen level!')
        self.__oxygen_level = round(value)

    @abstractmethod
    def miss(self, time_to_catch: int):
        to_reduce = round(self.oxygen_level - (time_to_catch * self.TIME_TO_REDUCE))
        if to_reduce < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = to_reduce
        if self.oxygen_level == 0:
            self.update_health_status()

    @abstractmethod
    def renew_oxy(self):
        self.oxygen_level = self.DIVER_OXYGEN_LEVEL

    def hit(self, fish: BaseFish):
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
            self.miss(fish.time_to_catch)
        else:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += fish.points
            if self.oxygen_level == 0:
                self.update_health_status()

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f'{self.__class__.__name__}: [Name: {self.name},'
                f' Oxygen level left: {self.oxygen_level},'
                f' Fish caught: {len(self.catch)},'
                f' Points earned: {self.competition_points}]')
