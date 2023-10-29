from project.pokemon import Pokemon

class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return f'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        result = (f'Pokemon Trainer {self.name}\n'
                  f'Pokemon count {len(self.pokemons)}\n')
        for p in self.pokemons:
            result += f'- {p.pokemon_details()}'
        return result
