pot = {
    'basti': {
        'pichu': {
            'lvl': 40,
            'evolution': 0,
            'location': [42,42,42]
        },
        'pikachu': {
            'lvl': 41,
            'evolution': 1,
            'location': [43,43,43]
        },
        'raichu': {
            'lvl': 42,
            'evolution': 2,
            'location': [44,44,44]
        }
    },
    'Dani': {
        'schiggy': {
            'lvl': 40,
            'evolution': 0,
            'location': [42,42,42]
        },
        'schillok': {
            'lvl': 41,
            'evolution': 1,
            'location': [43,43,43]
        },
        'turtok': {
            'lvl': 42,
            'evolution': 2,
            'location': [44,44,44]
        }
    },
    'Jeff': {
        'bisasam': {
            'lvl': 40,
            'evolution': 0,
            'location': [42,42,42]
        },
        'bisaknosp': {
            'lvl': 41,
            'evolution': 1,
            'location': [43,43,43]
        },
        'bisaflor': {
            'lvl': 42,
            'evolution': 2,
            'location': [44,44,44]
        }
    },
}

for trainer, trainer_info in pot.items():
    output = f'trainer: {trainer}\n'
    for pokemon, pokemon_info in trainer_info.items():
        output += f'    pokemon: {pokemon}\n'
        for key, val in pokemon_info.items():
            output += f'        {key}: {val}\n'
    print(output)




























fruits = ['banana', 'apple']
numbers = ['1', '2', '3', '4', '5']
zipped = [('banana', '1'), ('apple', '2')]
enumerated = [(0, ('banana', '1')), (1, ('apple', '2'))]
new_list = [(i, fruit, number * 2) for i, (fruit, number) in enumerate(zip(fruits, numbers))]

new_list = [(i, fruit, number * 2) for i, (fruit, number) in [(0, ('banana', '1')), (1, ('apple', '2'))]]

new_list = []
for i, (fruit, number) in [(0, ('banana', '1')), (1, ('apple', '2'))]:
    new_list.append((i, fruit, number * 2))

print(new_list)























