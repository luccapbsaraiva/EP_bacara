import random
import math
jogo_valido = True
dinheiro = 100
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
while jogo_valido:
     while dinheiro > 0:  # O jogo só ocorrerá enquanto o jogador tiver dinheiro
         aposta = int(input("Qual a quantia que deseja apostar?: "))
         if aposta > dinheiro: #Não deixar o jogador apostar mais do que tem
             print("Aposta excede suas fichas disponíveis.")
             aposta = int(input("Qual a quantia que deseja apostar?: "))
         else:
             pass
         quem_ganha = str(input("Quem você acha que vai ganhar: Jogador, Banca ou Empate?: "))   

         #Cartas do baralho
         cartas = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         carta_jogador_1 = random.choice(cartas)
         del(cartas[carta_jogador_1])
         carta_jogador_2 = random.choice(cartas)
         del(cartas[carta_jogador_2])
         carta_banca_1 = random.choice(cartas)
         del(cartas[carta_banca_1])
         carta_banca_2 = random.choice(cartas)
         del(cartas[carta_banca_2])
         soma_jogador = carta_jogador_1 + carta_jogador_2
         soma_banca = carta_banca_1 + carta_banca_2
         if soma_jogador >= 10:
             soma_jogador -= 10
         if soma_banca >= 10:
             soma_banca -= 10
         print("Sua mão é: {0} e {1}".format(tipo_de_carta(carta_jogador_1), tipo_de_carta(carta_jogador_2)))
         print("A mão da banca é: {0} e {1}".format(tipo_de_carta(carta_banca_1), tipo_de_carta(carta_banca_2)))
         print ('soma do jogador: {0}'. format(soma_jogador))
         print ('soma da banca: {0}'. format(soma_banca))
         xyz = input("Pressione enter para continuar. ")

         #Quando precisa de uma terceira carta
         if soma_jogador <= 5 and soma_banca != 9:
             carta_jogador_3 = random.choice(cartas)
             del(cartas[carta_jogador_3])
             soma_jogador += carta_jogador_3
             print("Sua nova carta é: {0}".format(tipo_de_carta(carta_jogador_3)))
             print ('nova soma do jogador {0}'. format(soma_jogador))
         if soma_banca <= 5 and soma_jogador != 9:
             carta_banca_3 = random.choice(cartas)
             del(cartas[carta_banca_3])
             soma_banca += carta_banca_3
             print("A nova carta da banca é: {0}".format(tipo_de_carta(carta_banca_3)))
             print ('nova soma da banca {0}'. format(soma_banca))

         #Para valores que ultrapassem nove
         if 10<= soma_jogador < 20:
             soma_jogador = (soma_jogador - 10)
         elif soma_jogador >= 20:
             soma_jogador = (soma_jogador-20) 
         if 10<= soma_banca < 20:
             soma_jogador = (soma_banca - 10)
         elif soma_banca >= 20:
             soma_banca = (soma_banca-20) 
             
         #O vencedor da partida e pagamento
         if soma_jogador > soma_banca:
             vencedor= 'Jogador'
             if vencedor == quem_ganha:
                 dinheiro += aposta
             else:
                 dinheiro -= aposta
         elif soma_jogador < soma_banca:
             vencedor = 'Banca'
             if vencedor == quem_ganha:
                 dinheiro += 0.95*aposta
             else: 
                 dinheiro -= aposta
         else: 
             vencedor = 'Empate'
             if vencedor == quem_ganha:
                 dinheiro += 8 * aposta
             else:
                 dinheiro -= aposta
         print ('Voce esta com {0} fichas'. format(dinheiro))
     print("Suas fichas acabaram.")
     jogo_valido = False    
