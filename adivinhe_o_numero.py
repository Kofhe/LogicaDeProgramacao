import random

numero_aleatorio = random.randint(0, 10)

Nome = input('Digite seu nome: ')
palpite_jogador = int(input("Adivinhe o número entre 0 e 10: "))
numero_tentativas = 0

while numero_aleatorio != palpite_jogador:
    numero_tentativas += 1

    if palpite_jogador > numero_aleatorio:
        print("Muito alto")
    else:
        print("Muito baixo")

    palpite_jogador = int(input("Adivinhe o número entre 0 e 10: "))

print("Parabéns, você acertou o número, em", numero_tentativas, "vezes")
print("Obrigado por jogar, " + Nome + "!")

recorde_tentativas = numero_tentativas
print ("Seu recorde de tentativas é:", recorde_tentativas)

print("Jogar novamente? (sim/não)")

resposta = "sim"
while resposta == "sim":
    numero_aleatorio = random.randint(0, 10)
    palpite_jogador = int(input("Adivinhe o número entre 0 e 10: "))
    numero_tentativas = 0

    while numero_aleatorio != palpite_jogador:
        numero_tentativas += 1
        if palpite_jogador > numero_aleatorio:
            print("Muito alto")
        else:
            print("Muito baixo")
            palpite_jogador = int(input("Adivinhe o número entre 0 e 10: "))
            print("Parabéns, você acertou o número, em", numero_tentativas, "vezes")

            recorde_tentativas = numero_tentativas
            print("Seu recorde de tentativas é:", recorde_tentativas)
    
resposta = "não"
if resposta == "não":
    print("Obrigado por jogar " + Nome)
