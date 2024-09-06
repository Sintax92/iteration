# stell dir vor wir wollen die zahlen 21 - 42 in einer liste abspeichern

topf = [21, 22, 23, 24, 25, ...]

topf = []
for i in range(21, 43):
    topf.append(i)

topf = [i for i in range(21, 43)]

topf2 = [i + 2 for i in range(10)]

topf2 = []
for i in range(10):
    topf2.append(i + 2)

topf3 = [i // 2 for i in range(3, 6)]

topf3 = []
for i in range(3, 6):
    topf3.append(i // 2)

topf4 = []
for element in ['a', 'b', 'c']:
    topf4.append(element * 2)

topf4 = [element * 2 for element in ['a', 'b', 'c']]

topf5 = []
for a, b in zip([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']):
    topf5.append(a * b)
topf5 = [a * b for a, b in zip([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])]

topf6 = [(a, b) for a, b in enumerate(['a', 'b', 'c', 'd', 'e'])]

topf6 = []
for a, b in enumerate(['a', 'b', 'c', 'd', 'e']):
    topf6.append((a, b))


topf7 = [element for element in sorted([4,6,2,5,7,2,1,4])]

topf7 = []
for element in sorted([4,6,2,5,7,2,1,4]):
    topf7.append(element)


topf8 = []
for i in range(44, 42, -1):
    iterable = [k for k in range(i)][::-1]
    topf8.append(iterable[-1])


topf8 = [[k for k in range(i)[::-1]][-1] for i in range(44, 42, -1)]
