import sys
pokemons = [pokemon.strip() for pokemon in sys.stdin]
print(len(pokemons) - len(set(pokemons)))