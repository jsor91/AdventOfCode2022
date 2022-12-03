with open("Day1Data.txt") as f:
    content = f.readlines()

calorie_list=[]
elf=1
calorie = 0
print(content)
for i in content:
    if i != "\n":
        number = int(i.rstrip())
        # print(number)
        calorie += number
        print(calorie)
    else:
        print("ELF" + str(elf) + ":" + str(calorie))
        calorie_list.append(calorie)
        calorie = 0
        elf += 1

print(calorie_list)
print(len(calorie_list))
print(max(calorie_list))
sorted_calorie_list = (sorted(calorie_list, reverse=True))
print(sorted_calorie_list)

calorie_big = 0
for x in range(3):
    calorie_big += sorted_calorie_list[x]

print(calorie_big)