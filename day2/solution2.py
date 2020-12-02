with open('input.txt', 'r') as reading:
    file_input = reading.read().split('\n')

correct = 0
for i in file_input:

    splittz = i.rsplit(' ', 2)

    boundaries = [int(i) for i in splittz[0].rsplit('-', 1)]
    character = splittz[1][0]
    passwd = splittz[2]
    
    count = 0
    index = 1
    for bokstav in passwd: 
        if bokstav == character: 
            if index in boundaries:
                count = count + 1
        index = index + 1

    if count == 1:
        correct = correct + 1

print(correct)