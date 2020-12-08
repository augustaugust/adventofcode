with open('day3/input.txt', 'r') as reading:
    grid = reading.read().split('\n')



def the_function(x_change, y_change):
    x = 0
    y = 0
    newgrid = []
    count = 0
    bredd = len(grid[0])

    for i in grid:
        if not y % y_change:
            if x > bredd-1:
                x = x - bredd 
            if i[x] == "#":
                newchar = "X"
                count = count + 1
            elif i[x] == ".":
                newchar = "O"
            
            str1 = ""
            new = list(i)
            new[x] = newchar
            for ele in new:  
                str1 += ele
            newgrid.append(str1)
            x = x + x_change
        else:
            newgrid.append(i)
        y = y + 1
    print("X change:" + str(x_change))
    print("Y change:" + str(y_change))
    print(count)
    return newgrid

grid1 = the_function(1,1)
grid2 = the_function(3,1)
grid3 = the_function(5,1)
grid4 = the_function(7,1)
grid5 = the_function(1,2)

for i in grid5:
    print(i)
