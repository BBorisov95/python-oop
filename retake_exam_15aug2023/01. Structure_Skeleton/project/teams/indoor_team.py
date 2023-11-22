from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    WIN_ADVANTAGE_POINTS = 145
    BUDGED = 500
    TYPE = 'IndoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, IndoorTeam.BUDGED)

    def win(self):
        self.wins += 1
        self.advantage += IndoorTeam.WIN_ADVANTAGE_POINTS
