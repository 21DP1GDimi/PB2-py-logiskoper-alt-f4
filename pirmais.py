liet_x = float(input("x:"))
liet_y = float(input("y:"))

if liet_x > -1 and liet_x < 3:
    if liet_y < 1 and liet_y > -2:
        print("iekšā")
    elif liet_y == 1 or liet_y == -2:
        print("uz līnijas")
    else:
        print("ārā")
elif liet_x == 3 or liet_x == -1:
    if liet_y < 1 and liet_y > -2:
        print("uz linijas")
    else:
        print("ārā")
else:
    print("ārā")
