with open("Day4Data.txt") as f:
    content = f.readlines()

# print(content)

data = []

for i in content:
    new_i = i.strip()
    data.append(new_i)

print(data)

elf1data = []
elf2data = []

for i in data:
    comma_marker = 0
    for j in range(len(i)):
        if i[j] == ",":
            comma_marker = j
            elf1shift = i[0:j]
            elf2shift = i[(j+1):len(i)]
            elf1data.append(elf1shift)
            elf2data.append(elf2shift)

print(elf1data)
print(elf2data)

elf1data_begin = []
elf1data_end = []
elf2data_begin = []
elf2data_end = []

for i in elf1data:
    # hyphen_marker = 0
    for j in range(len(i)):
        if i[j] == "-":
            hyphen_marker = j
            elf1begin = i[0:j]
            elf1end = i[(j+1):len(i)]
            elf1data_begin.append(elf1begin)
            elf1data_end.append(elf1end)

for i in elf2data:
    # hyphen_marker2 = 0
    for j in range(len(i)):
        if i[j] == "-":
            hyphen_marker2 = j
            elf2begin = i[0:j]
            elf2end = i[(j+1):len(i)]
            elf2data_begin.append(elf2begin)
            elf2data_end.append(elf2end)

print("Elf 1 begin shift: elf1data_begin")
print(elf1data_begin)
print(len(elf1data_begin))
print("Elf 1 end shift: elf1data_end")
print(elf1data_end)
print(len(elf1data_end))
print("Elf 2 begin shift: elf2data_begin")
print(elf2data_begin)
print(len(elf2data_begin))
print("Elf 2 end shift: elf2data_end")
print(elf2data_end)
print(len(elf2data_end))


shift_count = 0
for i in range(len(data)):
    print("---")
    print("Elf 1 shift: %s - %s:" % (elf1data_begin[i], elf1data_end[i]))
    print("Elf 2 shift: %s - %s:" % (elf2data_begin[i], elf2data_end[i]))
    print("Comparing Elf 1 Start Shift %s to %s" % (elf1data_begin[i], elf2data_begin[i]))
    print("Comparing Elf 1 End Shift %s to %s" % (elf1data_end[i], elf2data_end[i]))

    if elf1data_begin[i] < elf2data_begin[i]:
        print("Elf 1 starts earlier shift")
        if elf1data_end[i] < elf2data_end[i]:
            print("Different shifts")
        if elf1data_end[i] == elf2data_end[i]:
            print("Elf 1 ends same shift as Elf 2. ADD ONE")
            shift_count += 1
        if elf1data_end[i] > elf2data_end[i]:
            print("Elf 1 works over Elf 2 shifts. ADD ONE")
            shift_count += 1
    if elf1data_begin[i] == elf2data_begin[i]:
        print("Elf 1 starts same shift. ADD ONE")
        shift_count += 1

    if elf1data_begin[i] > elf2data_begin[i]:
        print("Elf 1 starts later shift")
        if elf1data_end[i] < elf2data_end[i]:
            print("Elf 2 works over Elf 1 shifts. ADD ONE")
            shift_count += 1
        if elf1data_end[i] == elf2data_end[i]:
            print("Elf 1 ends same shift as Elf 2. ADD ONE")
            shift_count += 1
        if elf1data_end[i] > elf2data_end[i]:
            print("Different shifts")

print(shift_count)
