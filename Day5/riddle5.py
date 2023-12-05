def task1(filename):
    with open(filename, "r") as file:
        seeds = list(map(int, file.readline().removeprefix("seeds: ").removesuffix("\n").split(" ")))

        #print(seeds)
        
        # empty line
        file.readline()

        # seed to soil
        max_entry = 0
        soils = dict() # key: soil, entry: seed 
        #for i in range(max_entry):
            #soils.update({i:i})
        
        print(file.readline())
        line = file.readline()
        while line != "\n":
            dest_range, source_range, range_length = line.split(" ")
            dest_range = int(dest_range)
            source_range = int(source_range)
            range_length = int(range_length)
            #print(dest_range, source_range, range_length)

            if (source_range + range_length) > max_entry:
                for i in range(max_entry, source_range + range_length):
                    soils.update({i: i})
                max_entry = source_range + range_length

            soil = range(dest_range, dest_range+range_length)
            seed = range(source_range, source_range + range_length)

            ##print(soil,seed)

            for i in range(int(range_length)):
                soils.update({seed[i]: soil[i]})
            line = file.readline()

        #print(soils)
        # soil to fertilizer
        print(file.readline())
        line = file.readline()

        
        fertilizers = dict()
        for i in range(max_entry):
            fertilizers.update({i:i})

        while line != "\n":
            dest_range, source_range, range_length = line.split(" ")
            dest_range = int(dest_range)
            source_range = int(source_range)
            range_length = int(range_length)
            #print(dest_range, source_range, range_length)

            if (source_range + range_length) > max_entry:
                for i in range(max_entry, source_range + range_length):
                    soils.update({i: i})
                    fertilizers.update({i:i})
                max_entry = source_range + range_length

            fertilizer = range(int(dest_range),int(dest_range)+int(range_length))
            soil = range(int(source_range),int(source_range) + int(range_length))

            ##print(fertilizer,soil)

            for i in range(int(range_length)):
                fertilizers.update({soil[i]: fertilizer[i]})
            line = file.readline()


        #print(fertilizers)


        # fertilizer to water
        print(file.readline())
        line = file.readline()
        waters = dict()
        for i in range(max_entry):
            waters.update({i:i})

        while line != "\n":
            dest_range, source_range, range_length = line.split(" ")
            dest_range = int(dest_range)
            source_range = int(source_range)
            range_length = int(range_length)
            #print(dest_range, source_range, range_length)

            if (source_range + range_length) > max_entry:
                for i in range(max_entry, source_range + range_length):
                    soils.update({i: i})
                    fertilizers.update({i: i})
                    waters.update({i: i})
                max_entry = source_range + range_length

            water = range(int(dest_range),int(dest_range)+int(range_length))
            fertilizer = range(int(source_range),int(source_range) + int(range_length))

            ##print(water,fertilizer)

            for i in range(int(range_length)):
                waters.update({fertilizer[i]: water[i]})
            line = file.readline()
        #print(waters)


        # water to light
        print(file.readline())
        line = file.readline()
        lights = dict()
        for i in range(max_entry):
            lights.update({i:i})

        while line != "\n":
            dest_range, source_range, range_length = line.split(" ")
            dest_range = int(dest_range)
            source_range = int(source_range)
            range_length = int(range_length)
            #print(dest_range, source_range, range_length)

            if (source_range + range_length) > max_entry:
                for i in range(max_entry, source_range + range_length):
                    soils.update({i: i})
                    fertilizers.update({i: i})
                    waters.update({i: i})
                    lights.update({i: i})
                max_entry = source_range + range_length

            light = range(int(dest_range),int(dest_range)+int(range_length))
            water = range(int(source_range),int(source_range) + int(range_length))

            ##print(light,water)

            for i in range(int(range_length)):
                lights.update({water[i]: light[i]})
            line = file.readline()


        # light to temperature
        print(file.readline())
        line = file.readline()
        temps = dict()
        for i in range(max_entry):
            temps.update({i:i})

        while line != "\n":
            dest_range, source_range, range_length = line.split(" ")
            dest_range = int(dest_range)
            source_range = int(source_range)
            range_length = int(range_length)
            #print(dest_range, source_range, range_length)

            if (source_range + range_length) > max_entry:
                for i in range(max_entry, source_range + range_length):
                    soils.update({i: i})
                    fertilizers.update({i: i})
                    waters.update({i: i})
                    lights.update({i: i})
                    temps.update({i: i})
                max_entry = source_range + range_length

            temp = range(int(dest_range),int(dest_range)+int(range_length))
            light = range(int(source_range),int(source_range) + int(range_length))

            ##print(light,water)

            for i in range(int(range_length)):
                temps.update({light[i]: temp[i]})
            line = file.readline()

        # temperature to humidity
        print(file.readline())
        line = file.readline()
        humidities = dict()
        for i in range(max_entry):
            humidities.update({i:i})

        while line != "\n":
            dest_range, source_range, range_length = line.split(" ")
            dest_range = int(dest_range)
            source_range = int(source_range)
            range_length = int(range_length)
            ##print(dest_range, source_range, range_length)

            if (source_range + range_length) > max_entry:
                for i in range(max_entry, source_range + range_length):
                    soils.update({i: i})
                    fertilizers.update({i: i})
                    waters.update({i: i})
                    lights.update({i: i})
                    temps.update({i: i})
                    humidities.update({i: i})
                max_entry = source_range + range_length
            humidity = range(int(dest_range),int(dest_range)+int(range_length))
            temp = range(int(source_range),int(source_range) + int(range_length))

            ##print(humidity,temp)

            for i in range(int(range_length)):
                humidities.update({temp[i]: humidity[i]})
            line = file.readline()
        # humitidy to location
        print(file.readline())
        line = file.readline()
        locations = dict()
        for i in range(max_entry):
            locations.update({i:i})

        while line != "\n" and line != "":
            dest_range, source_range, range_length = line.split(" ")
            dest_range = int(dest_range)
            source_range = int(source_range)
            range_length = int(range_length)
            ##print(dest_range, source_range, range_length)

            if (source_range + range_length) > max_entry:
                for i in range(max_entry, source_range + range_length):
                    soils.update({i: i})
                    fertilizers.update({i: i})
                    waters.update({i: i})
                    lights.update({i: i})
                    temps.update({i: i})
                    humidities.update({i: i})
                    locations.update({i: i})
                max_entry = source_range + range_length

            location = range(int(dest_range),int(dest_range)+int(range_length))
            humidity = range(int(source_range),int(source_range) + int(range_length))

            ##print(location,humidity)

            for i in range(int(range_length)):
                locations.update({humidity[i]: location[i]})
            line = file.readline()

        ##print(locations)

        results = []
        for seed in seeds:
            results.append(locations[humidities[temps[lights[waters[fertilizers[soils[seed]]]]]]])

        minimum = min(results)
        print(minimum, results, seeds[results.index(minimum)])

task1("input1")
        
