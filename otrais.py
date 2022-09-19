liet_x = float(input("x:"))
liet_y = float(input("y:"))

if liet_x > -5 and liet_x < 2:
    if liet_y < 3 and liet_y > -1:
        print("iekšā")
    elif liet_y == 3 or liet_y == -1:
        print("uz līnijas")
    else:
        print("ārā")
elif liet_x == 2 or liet_x == -5:
    if liet_y < 3 and liet_y > -1:
        print("uz linijas")
    else:
        print("ārā")
else:
    print("ārā")