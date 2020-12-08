with open('day5/input.txt', 'r') as reading:
        file_input = reading.read().split('\n')



boarding_passes = []

for i in file_input:

    #row
    row = i[:7]
    row = list(row)
    nums = range(0,128)
    while row:
        char = row.pop(0)
        if char:
            if char == 'F':
                nums = nums[0:len(nums)//2]
            elif char == 'B':
                nums = nums[len(nums)//2 if len(nums)%2==0 else ((len(nums)//2)+1):]
    row_number = list(nums)[0]

    #column
    col = i[3:]
    col = list(col)
    nums = range(0,8)
    while col:
        char = col.pop(0)
        if char:
            if char == 'L':
                nums = nums[0:len(nums)//2]
            elif char == 'R':
                nums = nums[len(nums)//2 if len(nums)%2==0 else ((len(nums)//2)+1):]
    col_number = list(nums)[0]

    boarding_passes.append((row_number,col_number))


def all_unique(lst):
  return len(lst) == len(set(lst))

test = [1,2,3,5,6]
print(all_unique(boarding_passes))
print(boarding_passes)

highest = 0
IDS = []
for i in boarding_passes:
    num = i[0]*8+i[1]
    IDS.append(num)
    if num > highest:
        highest = num


IDS.sort()
print(IDS)

nicenumbers = list(range(91,929))

inter = 0
for i in IDS:
    if not i == nicenumbers[inter]:
        print(i)
        break
    inter = inter + 1
