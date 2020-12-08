
def readandcreatesets():
    with open('day4/input.txt', 'r') as reading:
        file_input = reading.read().split('\n')

    all_sets = []
    tempset = {}
    count = 0
    while file_input:
        newline = file_input.pop()
        count = count + 1
        if newline:
            newline = newline.split()
            for i in newline:
                splitted = i.split(":")
                tempset[splitted[0]] = splitted[1]
        else:
            all_sets.append(tempset)
            tempset = {}
        if count == 1096:
            all_sets.append(tempset)
            tempset = {}
    return all_sets


def checksets(sets):
    count = 0
    newsetremix = []
    for i in sets:
        try: 
            if i["byr"] and i["iyr"] and i["eyr"] and i["hgt"] and i["hcl"] and i["ecl"] and i["pid"]:
                newsetremix.append(i)
        except:
            pass
    return newsetremix

def checksetsforREAL(sets):
    correct = 0
    for i in sets:
        count = 0

        byr = i["byr"]
        if 1920<= int(byr) <= 2002:
            count = count + 1
        
        iyr = i["iyr"]
        if 2010 <= int(iyr) <= 2020:
            count = count + 1

        eyr = i["eyr"]
        if 2020 <= int(eyr) <= 2030:
            count = count + 1
        
        hgt = i["hgt"]
        hgt_num = hgt[:-2]
        hgt_type = hgt[-2:]
        if hgt_type == "in":
            if 59 <= int(hgt_num) <= 76:
                count = count + 1
        if hgt_type == "cm":
            if 150 <= int(hgt_num) <= 193:
                count = count + 1
        
        hcl = i["hcl"]
        if hcl[0] == "#":
            if len(hcl[1:]) == 6:
                char_count = 0
                for ch in hcl[1:]:
                    if ch >= 'a' and ch <= 'f':
                        char_count = char_count + 1
                    elif ch >= '0' and ch <= '9':
                        char_count = char_count + 1
                if char_count == 6:
                    count = count + 1

        ecl = i["ecl"]
        if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":
            count = count + 1

        pid = i["pid"]
        if len(pid) == 9:
            if int(pid) > 0:
                count = count + 1

        if count == 7:
            correct = correct + 1

    return correct


sets = readandcreatesets()

sets = checksets(sets)

num_correct_sets = checksetsforREAL(sets)




