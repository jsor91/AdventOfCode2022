stack1 = ['D', 'L', 'V', 'T', 'M', 'H', 'F']
stack2 = ['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P']
stack3 = ['R', 'S', 'D', 'M', 'P', 'H']
stack4 = ['L', 'B', 'V', 'F']
stack5 = ['N', 'H', 'G', 'L', 'Q']
stack6 = ['W', 'B', 'D', 'G', 'R', 'M', 'P']
stack7 = ['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q']
stack8 = ['C', 'L', 'W']
stack9 = ['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T']

totalstack = [stack1,
              stack2,
              stack3,
              stack4,
              stack5,
              stack6,
              stack7,
              stack8,
              stack9]

# print(totalstack)

with open("Day5Data.txt") as f:
    content = f.readlines()

# print(content)

data = []
for i in content:
    new_i = i.strip()
    data.append(new_i)

data2 = []
print("DATA")
print(data)
for i in data:
    new_i = i.replace("move ", "")
    new_new_i = new_i.replace(" from ", ",")
    new_new_new_i = new_new_i.replace(" to ", "-")
    candy1 = new_new_new_i.split(",")

    data2.append(candy1)

print("DATA2")
print(data2)
# print("Move #, From stack #, To stack #")
data3 = []
for i in data2:
    # print(i[0])
    candy3 = i[1].split("-")
    candy3.insert(0, i[0])
    # print(candy3)
    data3.append(candy3)
print("DATA3")
print(data3)

for i in data3: #going through the sanitized data
    boxamount = int(i[0])
    fromstack = int(i[1])
    tostack = int(i[2])
    print("moving %s boxes from stack %s to stack %s" % (boxamount, fromstack, tostack))
    box = 0
    while box < boxamount:
        from_column = totalstack[fromstack-1] # from stack
        last_container = from_column[-1]
        to_column = totalstack[tostack-1] # to stack
        print("BEFORE")
        print(from_column)
        print(to_column)
        to_column.append(last_container) # to stack after
        del from_column[-1] # from stack after
        print("AFTER")
        print(from_column)
        print(to_column)
        box+= 1

print(totalstack)
stacknumber = 0
for i in totalstack:
    print(stacknumber + 1)
    print(i)
    stacknumber += 1




