with open('day6/input.txt', 'r') as reading:
        file_input = reading.read().split('\n')

groups = []
group = []
for i in file_input:
    if i:
        newline= list(i)
        group.append(newline)
    else:
        groups.append(group)
        group = []

def intersection(first, *others):
    return set(first).intersection(*others)

newgroup = []
for g in groups:
    first = g[0]
    others = g[1:]
    new = intersection(first, *others)
    newgroup.append(new)

total_yeses = 0
for i in newgroup:
    total_yeses = total_yeses + len(i)

print(total_yeses)