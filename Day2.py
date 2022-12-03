with open("Day2Data.txt") as f:
    content = f.readlines()

print(content)
shape_score = 0
for i in content:
    if i[2] == "X":
        shape_score += 1
    if i[2] == "Y":
        shape_score += 2
    if i[2] == "Z":
        shape_score += 3
print(shape_score)

# A/X: Rock
# B/Y: Paper
# C/Z: Scissors
# 0 lost, 3 draw, 6 win
# Part 2:
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

match_score = 0
for i in content:
    if i[0] == "A" and i[2] == "X":
        match_score += 3
    if i[0] == "A" and i[2] == "Y":
        match_score += 6
    if i[0] == "A" and i[2] == "Z":
        match_score += 0
    if i[0] == "B" and i[2] == "X":
        match_score += 0
    if i[0] == "B" and i[2] == "Y":
        match_score += 3
    if i[0] == "B" and i[2] == "Z":
        match_score += 6
    if i[0] == "C" and i[2] == "X":
        match_score += 6
    if i[0] == "C" and i[2] == "Y":
        match_score += 0
    if i[0] == "C" and i[2] == "Z":
        match_score += 3

print(match_score)

print(shape_score + match_score)
print("PART 2")

# A/X: Rock: 1
# B/Y: Paper: 2
# C/Z: Scissors: 3
# 0 lost, 3 draw, 6 win
# Part 2:
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

match_score2 = 0
shape_score2 = 0
for i in content:
    if i[0] == "A" and i[2] == "X":
        shape_score2 += 3
        match_score2 += 0
    if i[0] == "A" and i[2] == "Y":
        shape_score2 += 1
        match_score2 += 3
    if i[0] == "A" and i[2] == "Z":
        shape_score2 += 2
        match_score2 += 6
    if i[0] == "B" and i[2] == "X":
        shape_score2 += 1
        match_score2 += 0
    if i[0] == "B" and i[2] == "Y":
        shape_score2 += 2
        match_score2 += 3
    if i[0] == "B" and i[2] == "Z":
        shape_score2 += 3
        match_score2 += 6
    if i[0] == "C" and i[2] == "X":
        shape_score2 += 2
        match_score2 += 0
    if i[0] == "C" and i[2] == "Y":
        shape_score2 += 3
        match_score2 += 3
    if i[0] == "C" and i[2] == "Z":
        shape_score2 += 1
        match_score2 += 6

print(shape_score2)
print(match_score2)
print(shape_score2 + match_score2)