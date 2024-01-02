from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):

    TIME_TO_CATCH = 180

    def __init__(self, name, points):
        super().__init__(name, points, self.TIME_TO_CATCH)

    def fish_details(self):
        return super().fish_details()