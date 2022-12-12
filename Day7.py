with open("Day7Data.txt") as f:
    content = f.readlines()

# print(content)

data = []
for i in content:
    new_i = i.strip()
    data.append(new_i)

# print(data)

for i in data:
    print(i)
    root = []
    dir1 = []
    dir2 = []
    dir3 = []
    dir4 = []
    dir5 = []