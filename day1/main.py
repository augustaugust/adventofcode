output = []

with open('input.txt', 'r') as reading:
    file_input = reading.read().split('\n')

str_list = list(filter(None, file_input))

res = [int(i) for i in str_list]

answer = [0,0,0]

for i in res:
    for p in res:
        for r in res:
            if i + p + r == 2020:
                answer[0] = i
                answer[1] = p
                answer[2] = r

