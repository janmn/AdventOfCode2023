import re

def getSum():
    with open("input_day1_modified.txt", "rt") as file:
    #with open("test_input", "rt") as file:
        sum = 0
        for line in file:
            origin = line
            out = ""

            for i in range(len(line)):
                if line[i].isdigit():
                    out += str(line[i])
                else:
                    if line[i] == "e":
                        if i + 5 < len(line) and line[i:i+5] == "eight":
                            out += "8"
                    elif line[i] == "f":
                        if(i + 4 < len(line)):
                            if line[i:i+4] == "four":
                                out += "4"
                            if line[i:i+4] == "five":
                                out += "5"
                    elif line[i] == "n":
                        if(i + 4 < len(line) and line[i:i+4] == "nine"):
                            out += "9"
                    elif line[i] == "o":
                        if i + 3 < len(line) and line[i:i+3] == "one":
                            out += "1"
                    elif line[i] == "s":
                        if(i + 5 < len(line) and line[i:i+5] == "seven"):
                            out += "7"
                        if i + 3 < len(line) and line[i:i+3] == "six":
                            out += "6"
                    elif line[i] == "t":
                        if i + 5 < len(line) and line[i:i+5] == "three":
                            out += "3"
                        if i + 3 < len(line) and line[i:i+3] == "two":
                            out += "2"

            first = 0
            last = 0
            first_occ = True 
            for symbol in out:
                if symbol.isdigit() and first_occ:
                    first = symbol
                    last = symbol
                    first_occ = False
                elif symbol.isdigit():
                    last = symbol
            number = str(first) + str(last)
            if origin == line:
                print("Line: ", line, "Out: ", out, "Read Number: ", number)
                #i = 0
            else:
                print("Original: ", origin, "Out: ", out, "Read Number: ", number)
            sum += int(number)
        print("Sum: ", sum)

getSum()