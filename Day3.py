with open("Day3Data.txt") as f:
    content = f.readlines()

# print(content)

data = []

for i in content:
    new_i = i.strip()
    data.append(new_i)

print(data)

first_half = []
second_half = []

for i in data:
    # print(len(i))
    mid = len(i)//2
    # print(mid)
    first = i[0:mid]
    # print(first)
    second = i[mid:len(i)]
    # print(second)
    first_half.append(first)
    second_half.append(second)

print(first_half)
print(second_half)

points = []

for i in range(len(data)):
    unique = []
    for j in first_half[i]:
        if j in second_half[i]:
            unique.append(j)
    # print(unique)
    points.append(unique[0])

print(points)

pointdict = {"a": 1,
             "b": 2,
             "c": 3,
             "d": 4,
             "e": 5,
             "f": 6,
             "g": 7,
             "h": 8,
             "i": 9,
             "j": 10,
             "k": 11,
             "l": 12,
             "m": 13,
             "n": 14,
             "o": 15,
             "p": 16,
             "q": 17,
             "r": 18,
             "s": 19,
             "t": 20,
             "u": 21,
             "v": 22,
             "w": 23,
             "x": 24,
             "y": 25,
             "z": 26,
             "A": 27,
             "B": 28,
             "C": 29,
             "D": 30,
             "E": 31,
             "F": 32,
             "G": 33,
             "H": 34,
             "I": 35,
             "J": 36,
             "K": 37,
             "L": 38,
             "M": 39,
             "N": 40,
             "O": 41,
             "P": 42,
             "Q": 43,
             "R": 44,
             "S": 45,
             "T": 46,
             "U": 47,
             "V": 48,
             "W": 49,
             "X": 50,
             "Y": 51,
             "Z": 52,
             }

tot_points = 0

for i in points:
    tot_points += pointdict[i]

print(tot_points)