f = open('/Users/alina/PycharmProjects/adventofcode/aoc4/input.txt', 'r', encoding='utf-8-sig')
raw = f.read().split('\n')
data = []
data3 = []
for i in raw:
    data.append(i.split(','))
for i in data:
    first_elf_IDs_rough = i[0]
    second_elf_IDs_rough = i[1]

    first_elf_IDs = []
    second_elf_IDs = []

    for a in range(int(first_elf_IDs_rough.split('-')[0]), int(first_elf_IDs_rough.split('-')[1]) + 1):
        first_elf_IDs.append(a)

    for a in range(int(second_elf_IDs_rough.split('-')[0]), int(second_elf_IDs_rough.split('-')[1]) + 1):
        second_elf_IDs.append(a)

    data3.append([first_elf_IDs, second_elf_IDs])

result = 0
second_result = 0

for i in data3:
    first_IDs = i[0]
    second_IDs = i[1]

    first_flag = True
    second_flag = True

    for j in first_IDs:
        if j in second_IDs:
            pass
        else:
            first_flag = False
    for j in second_IDs:
        if j in first_IDs:
            pass
        else:
            second_flag = False

    if first_flag == True or second_flag == True:
        result += 1

for i in data3:
    first_IDs = i[0]
    second_IDs = i[1]

    flag = False
    final_flag = False
    for j in first_IDs:
        for k in second_IDs:
            if j == k:
                flag = True
                break
        if flag:
            final_flag = True
        else:
            final_flag = False
    if final_flag:
        second_result += 1


print(result, second_result)
