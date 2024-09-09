# region
# 1. transform to comprehension

numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number ** 2)

result = [num ** 2 for num in [1, 2, 3, 4, 5]]
# endregion

# region
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

result2 = [num for num in numbers if num % 2 == 0]  # kondition wird hinten dran geklebt
# endregion

# region
# dict
example_dict = {'label1': 'value1', 'label2': 'value2'}
numbers = [1, 2, 3, 4, 5]
squares_dict = {}
for number in numbers:
    squares_dict[number] = number ** 2

result3 = {number: number ** 2 for number in numbers}
# endregion

# region
# set
example_set = {1, 2, 3, 4, 5}
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = set()
for number in numbers:
    unique_squares.add(number ** 2)

result4 = {number ** 2 for number in numbers}
# endregion

# region
# nested
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = []
for row in matrix:
    for item in row:
        if item % 2 == 0:
            flat_list.append(item)

result5 = [item for row in matrix for item in row if item % 2 == 0]
# endregion

# region
# 2. transform to iteration
combos = [(x, y) for x in range(3) for y in range(3) if x != y]

result6 = []
for x in range(3):
    for y in range(3):
        if x != y:
            result6.append((x, y))
# endregion

# region
# 3. combinations
items3 = ['A', 'B', 'C']
expected_result = [('A', 'B'), ('A', 'C'), ('B', 'C')]
result7 = []

for item_a in items3:
    for item_b in items3:
        print(f'condition1: if {item_a} != {item_b} > {item_a != item_b}')
        print(f'condition2: if {(item_a, item_b)} not in current {result7} > {(item_a, item_b) in result7}')
        print(f'condition2: if {(item_b, item_a)} not in current {result7} > {(item_b, item_a) in result7}')
        if (item_a != item_b) and ((item_a, item_b) not in result7) and ((item_b, item_a) not in result7):
            result7.append((item_a, item_b))
print(result7)


for i in range(len(items3)):
    for j in range(i + 1, len(items3)):
        result7.append((items3[i], items3[j]))

result72 = [(items3[i], items3[j]) for i in range(len(items3)) for j in range(i + 1, len(items3))]


assert result7 == expected_result
# endregion

# region
# 4. permutations without repetition
items4 = ['A', 'B', 'C']
result = []
expected_result = [('')]
assert result == expected_result
# endregion

# region
# 5. permutations with repetition
items5 = ['X', 'Y', 'Z']
result = []
expected_result = [
    ('X', 'X'), ('X', 'Y'), ('X', 'Z'),
    ('Y', 'X'), ('Y', 'Y'), ('Y', 'Z'),
    ('Z', 'X'), ('Z', 'Y'), ('Z', 'Z')
]

result8 = [(items5[i], items5[j]) for i in range(len(items5)) for j in range(len(items5))]

assert result == expected_result
# endregion

expected_result2 = [
    ('X', 'Y'), ('X', 'Z'),
    ('Y', 'X'), ('Y', 'Z'),
    ('Z', 'X'), ('Z', 'Y'),
]

result9 = [(items5[i], items5[j]) for i in range(len(items5)) for j in range(len(items5)) if i != j]

expected_result3 = [
    ('X', 'X', 'X'), ('X', 'X', 'Y'), ('X', 'X', 'Z'),
    ('X', 'Y', 'X'), ('X', 'Y', 'Y'), ('X', 'Y', 'Z'),
    ('X', 'Z', 'X'), ('X', 'Z', 'Y'), ('X', 'Z', 'Z'),
    ('Y', 'X', 'X'), ('Y', 'X', 'Y'), ('Y', 'X', 'Z'),
    ('Y', 'Y', 'X'), ('Y', 'Y', 'Y'), ('Y', 'Y', 'Z'),
    ('Y', 'Z', 'X'), ('Y', 'Z', 'Y'), ('Y', 'Z', 'Z'),
    ('Z', 'X', 'X'), ('Z', 'X', 'Y'), ('Z', 'X', 'Z'),
    ('Z', 'Y', 'X'), ('Z', 'Y', 'Y'), ('Z', 'Y', 'Z'),
    ('Z', 'Z', 'X'), ('Z', 'Z', 'Y'), ('Z', 'Z', 'Z')
]

permutations = []

for i in items5:
    for j in items5:
        for k in items5:
            permutations.append((i, j, k))


permutations2 = [(i,j,k) for i in items5 for j in items5 for k in items5]

from itertools import product
permutations3 = list(product(items5, repeat=3))
