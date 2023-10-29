class SteamUser:

    def __init__(self, username: str, games: list):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hour) -> str:
        if game in self.games:
            self.played_hours += hour
            return f'{self.username} is playing {game}'
        return f'{game} is not in library'

    def buy_game(self, game) -> str:
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        return f'{game} is already in your library'

    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'
