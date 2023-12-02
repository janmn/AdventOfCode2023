# Read line per line
# split lines at ":" -> id, game
# split game at ";" -> [sets]
# split at "," -> [draws]
# check for <num of colored cubes> > <max of color>
    # if FALSE -> break / return FALSE
    # else -> return TRUE -> add id to sum
def riddle1():
    red = 12
    green = 13
    blue = 14

    with open('./puzzle_input.txt') as file:
        sum = 0
        for line in file:
            try:
                possible = True
                id, game = line.split(":")
                id = id.removeprefix("Game ")

                print("draw: " + str(game.split(";")))
                for draw in game.split(";"):
                    print("Set: " + str(draw.split(",")))
                    for set in draw.split(","):
                        set = set.removeprefix(" ")
                        cubes, color = set.split(" ")
                        color = color.removesuffix("\n")
                        #print(cubes, color)
                        if color == "red" and int(cubes) > red:
                            print("RED")
                            possible = False
                        if color == "green" and int(cubes) > green:
                            print("GREEN")
                            possible = False
                        if color == "blue" and int(cubes) > blue:
                            print("BLUE")
                            possible = False
                        print("\n")
                print(game + " : " + str(possible))
                if possible:
                    sum += int(id)
            except ValueError:
                print("Value Error: ", line)

        print("Sum: ", sum)


def riddle2():
    with open('./puzzle_input.txt') as file:
        sum = 0
        for line in file:
            red = 0
            green = 0
            blue = 0
                
            id, game = line.split(":")
            id = id.removeprefix("Game ")

            #print("draw: " + str(game.split(";")))
            for draw in game.split(";"):
                #print("Set: " + str(draw.split(",")))
                for set in draw.split(","):
                    set = set.removeprefix(" ")
                    cubes, color = set.split(" ")
                    color = color.removesuffix("\n")
                    #print(cubes, color)
                    if color == "red" and int(cubes) > red:
                        red = int(cubes)
                    if color == "green" and int(cubes) > green:
                        green = int(cubes)
                    if color == "blue" and int(cubes) > blue:
                        blue = int(cubes)
            print("Game: " + str(game) + ":\nRed: " + str(red) + " ; Green: " + str(green) + " ; Blue: " + str(blue))
            sum += (red*green*blue)
        print("Sum: ", sum)

riddle2()