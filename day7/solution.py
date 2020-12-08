with open('day7/input.txt', 'r') as reading:
        file_input = reading.read().split('\n')

items = []
mydict = {}
for row in file_input:
    row = row.split("contain")
    
    row[1] = row[1][:-1]
    row[1] = row[1].split(",")
    for i in row[1]:
        i = i.split()[:-1]
        print(i)
        i[1] = i[1] + " " + i[2]
        print(i)

    row[0] = row[0].split()[:-1]
    sstr = ""
    for i in row[0]:
        if sstr:
            sstr = sstr + " " + str(i)
        else:
            sstr = sstr + str(i) 

    mydict[sstr] = row[1]

#print(mydict)