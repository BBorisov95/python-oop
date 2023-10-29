class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage):
        if self.health <= damage:
            self.health = 0
            return f'{self.name} was defeated'
        self.health -= damage

    def heal(self, amount):
        self.health += amount