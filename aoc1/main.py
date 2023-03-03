f = open('/Users/alina/Desktop/input_new.txt', 'r', encoding='utf-8-sig')
sum = 0
max = 0
big1 = 0
big2 = 0
raw = f.read().split('\n\n\n')
for i in raw:
    sum = 0
    s_raw = i.split('\n')
    for j in s_raw:
        sum = sum + int(j)
    if sum > max:
        big2 = big1
        big1 = max
        max = sum
    else:
        if sum > big1:
            big2 = big1
            big1 = sum
        else:
            if sum > big2:
                big2 = sum

print(max, big1 + big2 + max)

