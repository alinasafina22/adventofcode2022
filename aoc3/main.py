f = open('/Users/alina/PycharmProjects/adventofcode/aoc3/input.txt', 'r', encoding='utf-8-sig')
'''
1 часть
raw = f.read().split('\n')
result = []
final_score = 0
alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'I':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
for i in raw:
    index_for_split = len(i)//2
    backpack1 = ''.join(set(i[:index_for_split]))
    backpack2 = ''.join(set(i[index_for_split:]))
    for j in backpack1:
        if backpack2.count(j) > 0:
            result.append(j)

for k in result:
    final_score += alphabet[k]

print(final_score)

'''
data_rough = f.read()

alphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'I':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

count = 0

per_line = data_rough.split('\n')

data = []

for i in range(int(len(per_line)/3)):
    data.append([per_line[count], per_line[count+1], per_line[count+2]])
    count += 3

same_letters = []

for i in data:
    same_letter = ''
    for rugzac in i:
        for letter in rugzac:
            if letter in i[0] and letter in i[1] and letter in i[2]:
                same_letter += letter
    same_letters.append(same_letter[0])

my_sum = 0

for i in same_letters:
    my_sum += alphabet[i]

print(my_sum)