with open('day6/input.txt', 'r') as reading:
        file_input = reading.read().split('\n')


groups = []
s = set()
for i in file_input:
    if i:
        newline= list(i)
        for item in newline:
            s.add(item)
    else:
        groups.append(s)
        print(s)
        s = set()

total_yeses = 0
for i in groups:
    total_yeses = total_yeses + len(i)

print(total_yeses)