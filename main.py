import os


select = input("Open, View, Edit, Exit: ")
count = 0

if select.startswith("Open"):
    contents = os.listdir("data")
    for item in contents:
        count = count + 1
        count_str = str(count)
        print(count_str + "." + item)

    open_file = input("Which file number would you like to open?")

    if open_file.startswith("1"):
        with open("data/temps.txt", "r") as file:
            temps = file.read()
            print("Temperatures: \n" + temps)
            number_str = temps.split(", ")
            numbers = [int(num_str) for num_str in number_str]
            to_do = input("Would you like to 1.Average or 2.Sort the data?")

            if to_do.startswith("1"):
                avg = sum(numbers) / len(numbers)
                avg = str(avg)
                print("The Average Temperature Is: " + avg)

            if to_do.startswith("2"):
                temps_str = temps.replace(",", "")
                number_str = temps_str.split()
                number_lst = [int(num_str) for num_str in number_str]
                number_lst.sort()
                number_lst = str(number_lst)
                print("Here is the sorted data: " + number_lst)
                select = input("Open, View, Edit, Exit: ")

    if open_file.startswith("2"):
        with open("data/wind.txt", "r") as file:
            wind = file.read()
            print("Wind Speed: \n" + wind)
            number_flt = wind.split(", ")
            numbers = [float(num_flt) for num_flt in number_flt]
            to_do = input("Would you like to 1.Average or 2.Sort the data?")

            if to_do.startswith("1"):
                avg = sum(numbers) / len(numbers)
                avg = str(avg)
                print("The Average Wind Speed Is: " + avg)
                select = input("Open, View, Edit, Exit: ")

            if to_do.startswith("2"):
                wind_str = wind.replace(",", "")
                number_str = wind_str.split()
                number_lst = [int(num_str) for num_str in number_str]
                number_lst.sort()
                number_lst = str(number_lst)
                print("Here is the sorted data: " + number_lst)
                select = input("Open, View, Edit, Exit: ")

    if open_file.startswith("3"):
        with open("data/rain.txt", "r") as file:
            rain = file.read()
            print("Rain(MM): \n" + rain)
            number_flt = rain.split(", ")
            numbers = [float(num_flt) for num_flt in number_flt]
            to_do = input("Would you like to 1.Average or 2.Sort the data?")

            if to_do.startswith("1"):
                avg = sum(numbers) / len(numbers)
                avg = str(avg)
                print("The Average Rainfall in MM is: " + avg)
                select = input("Open, View, Edit, Exit: ")

            if to_do.startswith("2"):
                rain_str = rain.replace(",", "")
                number_str = rain_str.split()
                number_lst = [int(num_str) for num_str in number_str]
                number_lst.sort()
                number_lst = str(number_lst)
                print("Here is the sorted data: " + number_lst)
                select = input("Open, View, Edit, Exit: ")



