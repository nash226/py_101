messed_pokemon = 'BulbAsaur-ChaRMAndeR-pikaCHU-chariZard-SQuirtlE'

list_1 = messed_pokemon.split('-')
pokedex = []
for pokemon in list_1:
    pokedex.append(pokemon.title())

pokedex.remove("Charizard")
 
print(pokedex) # ['Bulbasaur', 'Charmander', 'Pikachu', 'Squirtle']