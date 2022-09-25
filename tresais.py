"""
Programma, kas nosaka, kur atrodas punkts, figūras iekšā, uz līnijas vai ārā

Izveidoja: Gļebs Dimitrijevs DP2-1
"""

def nosaka_punktu(liet_x, liet_y):

    # Salīdzinam vērtības, meklējam puntkta atrašanas vietu
    if liet_x > 0 and liet_y > 0 and liet_y < liet_x * -1.5 + 3:
        print("iekšā figūrā")
    elif liet_x >= 0 and liet_y >= 0 and liet_y <= liet_x * -1.5 + 3:
        print("uz līnijas")
    else:
        print("ārā")
    

# Izsaucām programmu, ievadam lietotāja punkta datus
nosaka_punktu(liet_x = float(input("x:")), liet_y = float(input("y:")))