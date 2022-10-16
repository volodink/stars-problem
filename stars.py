# stars_data = "   " #-> WI
# stars_data = "0 0 0 0 0 0 0 0 0 0 0 0 0 10" #-> WI
# stars_data = "" #-> WI
# stars_data = "1 2 3 4 5 6 7 8 9 10" #-> OK
stars_data = "      10          6     6        4  5 6 7 8    9  4 5 6  6 5 4   10            " # -> OK
# stars_data = "      -10          2      3        4  5 6 7 8    9    10            " # -> OK

# stars_data = input()

print(stars_data)
if stars_data == "" or stars_data.strip() == "":
    print('Wrong input!')
    exit(0)

stars = [e for e in stars_data.split(" ") if e != ""]

stars_data_array = list(map(int, stars))

if (not stars_data_array) or (0 in stars_data_array) or (len([e for e in stars_data_array if e not in range(1, 11)]) != 0):
    print('Wrong input!')
    exit(0)

for s in stars_data_array:
    for _ in range(s):
        print("*", end=" ")
    print()
