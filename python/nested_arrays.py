

array1 = [
    ['Mario', 'Luigi', 'Bowser', [42]],
    ['Jack', 'Sam', 'Jonas', [43]],
    ['schiggy', 'Schillok', 'Turtok', [44]]
]

# for name1, name2, name3, level in array1:
#     print(name1, name2, name3, level[0])

array2 = [
    {
        "members": ['Mario', 'Luigi', 'Bowser'],
        "tags": [42],
        "platform": "Nintendo"
    },
    {
        "members": ['Jack', 'Sam', 'Jonas'],
        "tags": [43],
        "platform": "Cheyenne"
    },
    {
        "members": ['Schiggy', 'Schillok', 'Turtok'],
        "tags": [44],
        "platform": "Nintendo"
    }
]

for element in array2:
    member1 = element['members'][0]
    member2 = element['members'][1]
    member3 = element['members'][2]
    tags = element['tags'][0]
    platform = element['platform']
    out = f'members: {member1}, {member2}, {member3}\n'
    out += f'tags: {tags}\n'
    out += f'platform: {platform}\n'
    print(out)


array3 = {
    'mario': {
        "info": {
            "details": {
                "members": ['Mario', 'Luigi', 'Bowser'],
                "tags": [42],
                "platform": "Nintendo"
            }
        }
    },
    'stargate': {
        "info": {
            "details": {
                "members": ['Jack', 'Sam', 'Jonas'],
                "tags": [43],
                "platform": "Cheyenne"
            }
        }
    },
    'pokemon': {
        "info": {
            "details": {
                "members": ['Schiggy', 'Schillok', 'Turtok'],
                "tags": [44],
                "platform": "Nintendo"
            }
        }
    }
}

array4 = {
    'mario': {
        "info": {
            "details": {
                "members_data": [
                    {
                        "names": ('Mario', 'Luigi', 'Bowser'),
                        "attributes": {
                            "tags": [42],
                            "platform": "Nintendo",
                            "metadata": ("classic", ["jumping", "coins"], {"release_year": 1985})
                        }
                    }
                ]
            }
        }
    },
    'stargate': {
        "info": {
            "details": {
                "members_data": [
                    {
                        "names": ('Jack', 'Sam', 'Jonas'),
                        "attributes": {
                            "tags": [43],
                            "platform": "Cheyenne",
                            "metadata": ("sci-fi", ["adventure", "aliens"], {"release_year": 1997})
                        }
                    }
                ]
            }
        }
    },
    'pokemon': {
        "info": {
            "details": {
                "members_data": [
                    {
                        "names": ('Schiggy', 'Schillok', 'Turtok'),
                        "attributes": {
                            "tags": [44],
                            "platform": "Nintendo",
                            "metadata": ("monster", ["water", "battles"], {"release_year": 1996})
                        }
                    }
                ]
            }
        }
    }
}
