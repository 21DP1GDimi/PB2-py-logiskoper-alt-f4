"""
Programma, kas nosaka, kur atrodas punkts, figūras iekšā, uz līnijas vai ārā

Izveidoja: Gļebs Dimitrijevs DP2-1
"""

# importējam nepieciešamos moduļus
import math

# Izveidojam funkciju
def nosaka_punktu(liet_x, liet_y):

    # pierakstam apļa centra kordinātas
    apla_y = 0
    apla_x = 0

    # Salīdzinam vērtības, meklējam puntkta atrašanas vietu
    attalums_no_centra = math.sqrt(pow((liet_x - apla_x), 2) + pow((liet_y - apla_y), 2))
    
    if attalums_no_centra < pow(1, 2):
        print("iekšā")
    elif attalums_no_centra == pow(1, 2):
        print("uz līnijas")
    else:
        print("ārā")


# Izsaucām programmu, ievadam lietotāja punkta datus
nosaka_punktu(liet_x = float(input("x:")), liet_y = float(input("y:")))