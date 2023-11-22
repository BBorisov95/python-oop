from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    WIN_ADVANTAGE_POINTS = 115
    BUDGED = 1_000
    TYPE = 'OutdoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGED)

    def win(self):
        self.wins += 1
        self.advantage += OutdoorTeam.WIN_ADVANTAGE_POINTS
