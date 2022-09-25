"""
Programma, kas nosaka, kur atrodas punkts, figūras iekšā, uz līnijas vai ārā

Izveidoja: Gļebs Dimitrijevs DP2-1
"""

def nosaka_punktu(liet_x, liet_y):

    # Salīdzinam vērtības, meklējam puntkta atrašanas vietu
    if liet_x > -5 and liet_x < 2 and liet_y < 3 and liet_y > -1:
        print("iekšā")
    elif liet_x >= -5 and liet_x <= 2 and liet_y == 3 or liet_y == -1 or liet_y <= 3 and liet_y >= -1 and liet_x == -5 or liet_x == 2:
        print("uz linijas")
    else:
        print("ārā")
    

# Izsaucām programmu, ievadam lietotāja punkta datus
nosaka_punktu(liet_x = float(input("x:")), liet_y = float(input("y:")))
