m0 = [99, 67, 92, 61, 83, 64, 98]
m1 = [78, 74, 88, 89, 50]
m2 = [98, 91]
m3 = [59, 72, 94, 91, 79, 88, 94, 51]
m4 = [95, 72, 78]
m5 = [76]
m6 = [69, 60, 53, 89, 71, 88]
m7 = [72, 54, 63, 80]

m0_length = []
m1_length = []
m2_length = []
m3_length = []
m4_length = []
m5_length = []
m6_length = []
m7_length = []

for j in range(10000):
    print(j)

    m0_length.append(len(m0))
    for i in range(len(m0)):
        m0[i] = m0[i] * 17
        # m0[i] = int(m0[i]/3)
        if m0[i] % 3 == 0:
            m4.append(m0[i])
        else:
            m2.append(m0[i])
    m0 = []

    m1_length.append(len(m1))
    for i in range(len(m1)):
        m1[i] = m1[i] * 11
        # m1[i] = int(m1[i] / 3)
        if m1[i] % 5 == 0:
            m3.append(m1[i])
        else:
            m5.append(m1[i])
    m1 = []

    m2_length.append(len(m2))
    for i in range(len(m2)):
        m2[i] = m2[i] + 4
        # m2[i] = int(m2[i] / 3)
        if m2[i] % 2 == 0:
            m6.append(m2[i])
        else:
            m4.append(m2[i])
    m2 = []

    m3_length.append(len(m3))
    for i in range(len(m3)):
        m3[i] = m3[i] ** 2
        # m3[i] = int(m3[i] / 3)
        if m3[i] % 13 == 0:
            m0.append(m3[i])
        else:
            m5.append(m3[i])
    m3 = []

    m4_length.append(len(m4))
    for i in range(len(m4)):
        m4[i] = m4[i] + 7
        # m4[i] = int(m4[i] / 3)
        if m4[i] % 11 == 0:
            m7.append(m4[i])
        else:
            m6.append(m4[i])
    m4 = []

    m5_length.append(len(m5))
    for i in range(len(m5)):
        m5[i] = m5[i] + 8
        # m5[i] = int(m5[i] / 3)
        if m5[i] % 17 == 0:
            m0.append(m5[i])
        else:
            m2.append(m5[i])
    m5 = []

    m6_length.append(len(m6))
    for i in range(len(m6)):
        m6[i] = m6[i] + 5
        # m6[i] = int(m6[i] / 3)
        if m6[i] % 19 == 0:
            m7.append(m6[i])
        else:
            m1.append(m6[i])
    m6 = []

    m7_length.append(len(m7))
    for i in range(len(m7)):
        m7[i] = m7[i] + 3
        # m7[i] = int(m7[i] / 3)
        if m7[i] % 7 == 0:
            m1.append(m7[i])
        else:
            m3.append(m7[i])
    m7 = []
#
#     print("Monkey 0: ")
#     print(m0)
#     print("Monkey 1: ")
#     print(m1)
#     print("Monkey 2: ")
#     print(m2)
#     print("Monkey 3: ")
#     print(m3)
#     print("Monkey 4: ")
#     print(m4)
#     print("Monkey 5: ")
#     print(m5)
#     print("Monkey 6: ")
#     print(m6)
#     print("Monkey 7: ")
#     print(m7)
#
# print(m0_length)
# print(m1_length)
# print(m2_length)
# print(m3_length)
# print(m4_length)
# print(m5_length)
# print(m6_length)
# print(m7_length)

def find_count(length):
    total_count = 0
    for i in length:
        total_count += i
    print(total_count)

print("Monkey 0:")
find_count(m0_length)
print("Monkey 1:")
find_count(m1_length)
print("Monkey 2:")
find_count(m2_length)
print("Monkey 3:")
find_count(m3_length)
print("Monkey 4:")
find_count(m4_length)
print("Monkey 5:")
find_count(m5_length)
print("Monkey 6:")
find_count(m6_length)
print("Monkey 7:")
find_count(m7_length)
