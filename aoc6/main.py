f = open('/Users/alina/PycharmProjects/adventofcode/aoc6/input.txt', 'r', encoding='utf-8-sig')
new_list = f.read()

for i in range(14, len(new_list)):
    if len(set(new_list[i - 14:i])) == 14:
        print(i)
        break