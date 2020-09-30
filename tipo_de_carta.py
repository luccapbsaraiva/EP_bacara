import random
import math
def tipo_de_carta(carta):
    cartas_altas = ["Dez", "Valete", "Dama", "Rei"]
    if carta == 1:
        tipo = "Ás"
    elif carta == 2:
        tipo = "Dois"
    elif carta == 3:
        tipo = "Tres"
    elif carta == 4:
        tipo = "Quatro"
    elif carta == 5:
        tipo = "Cinco"
    elif carta == 6:
        tipo = "Seis"
    elif carta == 7:
        tipo = "Sete"
    elif carta == 8:
        tipo = "Oito"
    elif carta == 9:
        tipo = "Nove"
    else:
        tipo = random.choice(cartas_altas)
    return tipo





