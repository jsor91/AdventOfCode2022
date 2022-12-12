with open("Day8Data.txt") as f:
    content = f.readlines()

data = []

for i in content:
    new_i = i.strip()
    data.append(new_i)

print(data)


easttrees = []
east_tree_count = 0
# Find from East
# bigtree = 1
row_number = 0
for row in data:
    east_tree_count += 1
    bigtree = row[0]
    # print("bigtree")
    # print(bigtree)
    row_number += 1
    column_number = 1
    first_tree = str(column_number) + "," + str(row_number)
    easttrees.append(first_tree)
    for current_tree in row:
        # print("Tree %s , %s" % (row_number, column_number))
        # print("Current bigtree is: %s" % bigtree)
        if current_tree > bigtree:
            # print("%s is bigger than %s" % (current_tree, bigtree))
            coordinate = str(column_number) + "," + str(row_number)
            easttrees.append(coordinate)
            bigtree = current_tree
            east_tree_count += 1

        column_number += 1

print("From the east")
print(easttrees)
print(east_tree_count)

westtrees = []
west_tree_count = 0
row_number = 0
# Find from West
for row in data:
    west_tree_count += 1
    reverse_row = (row[::-1])
    bigtree = reverse_row[0]
    # print("bigtree")
    # print(bigtree)
    # print(reverse_row)
    row_number += 1
    column_number = 99
    first_tree = str(column_number) + "," + str(row_number)
    westtrees.append(first_tree)
    for current_tree in reverse_row:
        # print("Tree %s , %s" % (row_number, column_number))
        # print("Current bigtree is: %s" % bigtree)
        if current_tree > bigtree:
            # print("%s is bigger than %s" % (current_tree, bigtree))
            coordinate = str(column_number) + "," + str(row_number)
            westtrees.append(coordinate)
            bigtree = current_tree
            west_tree_count += 1

        column_number -= 1

print("From the west")
print(westtrees)
print(west_tree_count)


new_data = []
#Redo data to columns

for column in range(99):
    column_string = ""
    # print(int(column)+1)
    for row in data:
        digit = row[column]
        column_string = column_string + digit
    # print(column_string)
    new_data.append(column_string)

print(new_data)


northtrees = []
north_tree_count = 0

#Find from north

column_number = 0
for column in new_data:
    north_tree_count += 1
    bigtree = column[0]
    # print("bigtree")
    # print(bigtree)
    column_number += 1
    row_number = 1
    first_tree = str(column_number) + "," + str(row_number)
    northtrees.append(first_tree)
    for current_tree in column:
        # print("Tree %s , %s" % (column_number, row_number))
        # print("Current bigtree is: %s" % bigtree)
        if current_tree > bigtree:
            # print("%s is bigger than %s" % (current_tree, bigtree))
            coordinate = str(column_number) + "," + str(row_number)
            northtrees.append(coordinate)
            bigtree = current_tree
            north_tree_count += 1

        row_number += 1

print("From the north")
print(northtrees)
print(north_tree_count)

southtrees = []
south_tree_count = 0

#Find from south

column_number = 0
for column in new_data:
    south_tree_count += 1
    reverse_column = (column[::-1])
    # print(reverse_column)
    bigtree = reverse_column[0]
    # print("bigtree")
    # print(bigtree)
    column_number += 1
    row_number = 99
    first_tree = str(column_number) + "," + str(row_number)
    southtrees.append(first_tree)
    for current_tree in reverse_column:
        # print("Tree %s , %s" % (column_number, row_number))
        # print("Current bigtree is: %s" % bigtree)
        # print("Tree is: %s" % current_tree)
        if current_tree > bigtree:
            # print("%s is bigger than %s" % (current_tree, bigtree))
            coordinate = str(column_number) + "," + str(row_number)
            southtrees.append(coordinate)
            bigtree = current_tree
            south_tree_count += 1

        row_number -= 1

print("From the south")
print(southtrees)
print(south_tree_count)

print("----------------------")
print("\n")
print("----------------------")

print("east")
print(len(easttrees))
print(easttrees)
print("west")
print(len(westtrees))
print(westtrees)
print("north")
print(len(northtrees))
print(northtrees)
print("south")
print(len(southtrees))
print(southtrees)

combined_trees = []

for i in easttrees:
    combined_trees.append(i)

print(combined_trees)
print(len(combined_trees))

for i in westtrees:
    combined_trees.append(i)

print(combined_trees)
print(len(combined_trees))

for i in northtrees:
    combined_trees.append(i)

print(combined_trees)
print(len(combined_trees))

for i in southtrees:
    combined_trees.append(i)

print(combined_trees)
print(len(combined_trees))

unique_trees = []
duplicate_trees = []

for i in combined_trees:
    if i in unique_trees:
        duplicate_trees.append(i)
    if i not in unique_trees:
        unique_trees.append(i)


print("FINAL")
print(unique_trees)
print(len(unique_trees))
print(duplicate_trees)
print(len(duplicate_trees))