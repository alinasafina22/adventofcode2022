'''
A for камень, B for бумага, and C for ножницы
X for камень, Y for бумага, and Z for ножницы
1 for камень, 2 for бумага, and 3 for ножницы
0 if you lost, 3 if the round was a draw, and 6 if you won
2 задание
X проиграть, Y ничья , and Z нужно выграть.
'''

f = open('/Users/alina/PycharmProjects/adventofcode/aoc2/input.txt', 'r', encoding='utf-8-sig')
total_score = 0
final_score = 0
raw = f.read().split('\n')
for i in raw:
    total_score = 0
    column = i.split(' ')
    if column[0] == 'A':
        if column[1] == 'X':
            total_score = 0 + 3
        elif column[1] == 'Y':
            total_score = 3 + 1
        elif column[1] == 'Z':
            total_score = 6 + 2
    elif column[0] == 'B':
        if column[1] == 'X':
            total_score = 0 + 1
        elif column[1] == 'Y':
            total_score = 3 + 2
        elif column[1] == 'Z':
            total_score = 6 + 3
    elif column[0] == 'C':
        if column[1] == 'X':
            total_score = 0 + 2
        elif column[1] == 'Y':
            total_score = 3 + 3
        elif column[1] == 'Z':
            total_score = 6 + 1
    final_score += total_score


print(final_score)


