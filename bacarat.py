import random
import math
jogo_valido = True
dinheiro = 100
while jogo_valido:
    while dinheiro > 0:  # O jogo só ocorrerá enquanto o jogador tiver dinheiro
        aposta = int(input("Qual a quantia que deseja apostar?: "))
        if aposta > dinheiro: #Não deixar o jogador apostar mais do que tem
            print("Aposta excede suas fichas disponíveis.")
            aposta = int(input("Qual a quantia que deseja apostar?: "))
        else:
            pass
        quem_ganha = str(input("Quem você acha que vai ganhar: Jogador, Banca ou será empate?: "))
        carta_jogador_1 = random.randint(1, 52)
        carta_jogador_2 = random.randint(1, 52)
        carta_banca_1 = random.randint(1, 52)
        carta_banca_2 = random.randint(1, 52)
        def valor_carta(carta):
            for carta in range(1, 5):
                valor = 1
                tipo_carta = "Ás"
            for carta in range(5, 9):
                valor = 2
                tipo_carta = "2"
            for carta in range(9, 13):
                valor = 3
                tipo_carta = "3"
            for carta in range(13, 17):
                valor = 4
                tipo_carta = "4"
            for carta in range(17, 21):
                valor = 5
                tipo_carta = "5"
            for carta in range(21, 25):
                valor = 6
                tipo_carta = "6"
            for carta in range(25, 29):
                valor = 7
                tipo_carta = "7"
            for carta in range(29, 33):
                valor = 8
                tipo_carta = "8"
            for carta in range(33, 37):
                valor = 9
                tipo_carta = "9"
            for carta in range(37, 53):
                valor = 0
            return valor
        soma_jogador = valor_carta(carta_jogador_1) + valor_carta(carta_jogador_2)
        soma_banca =  valor_carta(carta_banca_1) + valor_carta(carta_banca_2)
        # Inserir aqui avaliação de possivel terceira carta
        # Tanto para banca quanto para jogador
        if 10<= soma_jogador < 20:
            soma_jogador = (soma_jogador - 10)
        elif soma_jogador >= 20:
            soma_jogador = (soma_jogador-20)

    
