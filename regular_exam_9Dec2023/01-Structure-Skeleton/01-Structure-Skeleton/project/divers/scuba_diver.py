from project.divers.base_diver import BaseDiver


class ScubaDiver (BaseDiver):
    DIVER_OXYGEN_LEVEL = 540
    TIME_TO_REDUCE = 0.3

    def __init__(self, name):
        super().__init__(name, self.DIVER_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        super().miss(time_to_catch)

    def renew_oxy(self):
        super().renew_oxy()
