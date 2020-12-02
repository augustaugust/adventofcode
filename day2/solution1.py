with open('input.txt', 'r') as reading:
    file_input = reading.read().split('\n')

correct = 0
for i in file_input:

    splittz = i.rsplit(' ', 2)

    boundaries = [int(i) for i in splittz[0].rsplit('-', 1)]
    character = splittz[1][0]
    passwd = splittz[2]

    count = 0
    for bokstav in passwd: 
        if bokstav == character: 
            count = count + 1

    if boundaries[0] <= count and count <= boundaries[1]:
        correct = correct + 1

print(correct)