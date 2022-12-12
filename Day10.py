with open("Day10Data.txt") as f:
    content = f.readlines()

# print(content)

data = []
for i in content:
    new_i = i.strip()
    data.append(new_i)

print(data)
action = []
value = []
signal = []
for i in data:
    if "noop" in i:
        action.append("noop")
        value.append(0)
    if "addx" in i:
        action.append("addx")
        digits = i.replace("addx ","")
        value.append(int(digits))

print(action)
print(value)
x_value_list = []

cycle = 1
x_value = 1
print("Cycle %s: %s" % (cycle, x_value))
for i in range(len(action)):
    if action[i] == "noop":
        cycle += 1
        x_value += value[i]
        print("Cycle %s: %s" % (cycle, x_value))
        x_value_list.append(x_value)
    if action[i] == "addx":
        cycle += 1
        print("Cycle %s: %s" % (cycle, x_value))
        x_value_list.append(x_value)
        cycle += 1
        x_value += value[i]
        print("Cycle %s: %s" % (cycle, x_value))
        x_value_list.append(x_value)

#
# signal = []
# signal.append(20 * 21)
# signal.append(60 * 21)
# signal.append(100 * 21)
# signal.append(140 * 21)
# signal.append(180 * 14)
# signal.append(220 * 17)
#
# print(signal)
# total = 0
# for i in signal:
#     total += i
#
# print(total)

print(x_value_list)
print(len(x_value_list))

x_value_list1 = x_value_list[0:40]
x_value_list2 = x_value_list[40:80]
x_value_list3 = x_value_list[80:120]
x_value_list4 = x_value_list[120:160]
x_value_list5 = x_value_list[160:200]
x_value_list6 = x_value_list[200:240]


print(x_value_list1)
print(len(x_value_list1))
print(x_value_list2)
print(len(x_value_list2))
print(x_value_list3)
print(len(x_value_list3))
print(x_value_list4)
print(len(x_value_list4))
print(x_value_list5)
print(len(x_value_list5))
print(x_value_list6)
print(len(x_value_list6))

def writing_lines(list):
    string = ""
    for i in range(len(list)):
        # print("Comparing x coordinate: %s and value: %s" % (i,list[i]))
        if i == (list[i]) or i == (list[i]+1) or i == (list[i]+2):
            string = string + "#"
        else:
            string = string + " "

    print(string)

writing_lines(x_value_list1)
writing_lines(x_value_list2)
writing_lines(x_value_list3)
writing_lines(x_value_list4)
writing_lines(x_value_list5)
writing_lines(x_value_list6)


#
#
#
# line1 = []
# line2 = []
# line3 = []
# line4 = []
#
# for i in x_value_list1:
#     if i == (x_value_list1[i]) or i == (x_value_list1[i]+1) or i == (x_value_list1[i]+2):
#         line1.append("#")
#     else:
#         line1.append(".")
# for i in x_value_list2:
#     if i == (x_value_list2[i]) or i == (x_value_list2[i]+1) or i == (x_value_list2[i]+2):
#         line2.append("#")
#     else:
#         line2.append(".")
# for i in x_value_list3:
#     if i == (x_value_list3[i]) or i == (x_value_list3[i]+1) or i == (x_value_list3[i]+2):
#         line3.append("#")
#     else:
#         line3.append(".")
# for i in x_value_list4:
#     if i == (x_value_list4[i]) or i == (x_value_list4[i]+1) or i == (x_value_list4[i]+2):
#         line4.append("#")
#     else:
#         line4.append(".")
#
# print(line1)
# print(line2)
# print(line3)
# print(line4)
#
# line1_text = "['#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.']"
# line1_text1 = line1_text.replace("[","")
# line1_text2 = line1_text1.replace("]","")
# line1_text3 = line1_text2.replace("'","")
# line1_text4 = line1_text3.replace(" ","")
# line1_text5 = line1_text4.replace(",","")
#
# line2_text = "['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#']"
# line2_text1 = line2_text.replace("[","")
# line2_text2 = line2_text1.replace("]","")
# line2_text3 = line2_text2.replace("'","")
# line2_text4 = line2_text3.replace(" ","")
# line2_text5 = line2_text4.replace(",","")
#
# line1_text = "['#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.']"
# line1_text1 = line1_text.replace("[","")
# line1_text2 = line1_text1.replace("]","")
# line1_text3 = line1_text2.replace("'","")
# line1_text4 = line1_text3.replace(" ","")
# line1_text5 = line1_text4.replace(",","")
#
# line1_text = "['#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.']"
# line1_text1 = line1_text.replace("[","")
# line1_text2 = line1_text1.replace("]","")
# line1_text3 = line1_text2.replace("'","")
# line1_text4 = line1_text3.replace(" ","")
# line1_text5 = line1_text4.replace(",","")
#
#
#
#
#
# print(line1_text5)
# print(line2_text5)
#
