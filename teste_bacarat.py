import random
import math
jogo_valido = True
dinheiro = 10000
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
numero_jogadores = int(input('Quantos jogadores irão jogar: 1 ou 2?: '))
if numero_jogadores == 2:
    dinheiro = 10000
    dinheiro_2 = 10000
    print('O jogador 1 tem {0} fichas'.format(dinheiro))
    print('O jogador 2 tem {0} fichas'.format(dinheiro_2))
elif numero_jogadores == 1:
    dinheiro = 10000
    print('O jogador 1 tem {0} fichas'.format(dinheiro))
while jogo_valido:
    if numero_jogadores == 2:
        if dinheiro > 0 or dinheiro_2 > 0:  # O jogo só ocorrerá enquanto um dos jogadores tiver dinheiro
            aposta = int(input("Qual a quantia que o jogador 1 deseja apostar?: "))
            aposta_2 = int(input("Qual a quantia que o jogador 2 deseja apostar?: "))
            if aposta > dinheiro: #Não deixar o jogador apostar mais do que tem
                print("Aposta do jogador 1 excede suas fichas disponíveis.")
                aposta = int(input("Qual a quantia que o jogador 1 deseja apostar?: "))
            elif aposta_2 > dinheiro_2:
                print("Aposta do jogador 2 excede suas fichas disponíveis.")
                aposta_2 = int(input("Qual a quantia que o jogadr 2 deseja apostar?: "))
            quem_ganha = str(input("Quem o jogador 1 acha que vai ganhar: Jogador, Banca ou Empate?: "))
            quem_ganha_2 = str(input("Quem o jogador 2 acha que vai ganhar: Jogador, Banca ou Empate?: "))   
            if quem_ganha not in ['Jogador', 'jogador', 'Banca', 'banca', 'Empate', 'empate']:
                print('jogador 1, não é possível apostar nesse resultado')
                quem_ganha = str(input("Quem o jogador 1 acha que vai ganhar: Jogador, Banca ou Empate?: "))
            elif quem_ganha_2 not in ['Jogador', 'jogador', 'Banca', 'banca', 'Empate', 'empate']:
                print('jogador 2, não é possível apostar nesse resultado')
                quem_ganha_2 = str(input("Quem o jogador 2 acha que vai ganhar: Jogador, Banca ou Empate?: "))

    elif numero_jogadores == 1:
        if dinheiro > 0:
            aposta = int(input("Qual a quantia que o jogador 1 deseja apostar?: "))
            if aposta > dinheiro: #Não deixar o jogador apostar mais do que tem
                print("Aposta excede suas fichas disponíveis.")
                aposta = int(input("Qual a quantia que deseja apostar?: "))
            quem_ganha = str(input("Quem o jogador 1 acha que vai ganhar: Jogador, Banca ou Empate?: "))
            if quem_ganha not in ['Jogador', 'jogador', 'Banca', 'banca', 'Empate', 'empate']:
                print('jogador 1, não é possível apostar nesse resultado')
                quem_ganha = str(input("Quem o jogador 1 acha que vai ganhar: Jogador, Banca ou Empate?: "))
         #Cartas do baralho
    cartas = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]*8
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
    carta_3j = False
        #Quando precisa de uma terceira carta
    if soma_jogador <= 5 and soma_banca != 9:
        carta_jogador_3 = random.choice(cartas)
        del(cartas[carta_jogador_3])
        soma_jogador += carta_jogador_3
        carta_3j = True
        #Para valores que ultrapassem nove 
        if 10<= soma_jogador:
            soma_jogador -= 10
        print("Sua nova carta é: {0}".format(tipo_de_carta(carta_jogador_3)))
        print ('nova soma do jogador é {0}'. format(soma_jogador))
    if soma_banca < 6:
        if carta_3j == False and soma_banca <= 5:
            carta_banca_3 = random.choice(cartas)
            del(cartas[carta_banca_3])
            soma_banca += carta_banca_3
        elif carta_3j == True:
            if soma_banca == 0 or soma_banca==1 or soma_banca==2:
                carta_banca_3 = random.choice(cartas)
                del(cartas[carta_banca_3])
                soma_banca += carta_banca_3
            elif soma_banca==3 and carta_jogador_3 != 8:
                carta_banca_3 = random.choice(cartas)
                del(cartas[carta_banca_3])
                soma_banca += carta_banca_3
            elif soma_banca ==4 and (carta_jogador_3 != 0 and carta_jogador_3 != 1 and carta_jogador_3 != 8 and carta_jogador_3 != 9):
                carta_banca_3 = random.choice(cartas)
                del(cartas[carta_banca_3])
                soma_banca += carta_banca_3
            elif soma_banca ==5 and (carta_jogador_3 == 4 and carta_jogador_3 == 5 and carta_jogador_3 == 6 and carta_jogador_3 == 7):
                carta_banca_3 = random.choice(cartas)
                del(cartas[carta_banca_3])
                soma_banca += carta_banca_3
            else: 
                pass
            #Para valores que ultrapassem nove
        if 10<= soma_banca:
            soma_banca -= 10
        print("A nova carta da banca é: {0}".format(tipo_de_carta(carta_banca_3)))
        print ('nova soma da banca é {0}'.format(soma_banca))
    
    #O vencedor da partida e pagamento
    if soma_jogador > soma_banca:
        vencedor= ['Jogador', 'jogador']
        if quem_ganha in vencedor:
            dinheiro += aposta - (0.0124*aposta)
        else:
            dinheiro -= aposta
    elif soma_jogador < soma_banca:
        vencedor = ['Banca', 'banca']
        if quem_ganha in vencedor:
            dinheiro += (0.95*aposta) - 0.0106*(0.95*aposta)
        else: 
            dinheiro -= aposta
    else: 
        vencedor = ['Empate', 'empate']
        if quem_ganha in vencedor:
            dinheiro += 8 * aposta - 0.1436*(8*aposta)
        else:
            dinheiro -= aposta
    print ('Voce esta com {0} fichas'.format(dinheiro))
print("Suas fichas acabaram.")
jogo_valido = False    
