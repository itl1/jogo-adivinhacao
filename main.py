import random

numero_secreto = random.randint(1, 10)
tentativas = 0

print("Jogo de Adivinhação")
print("Tente adivinhar o número de 1 a 10")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
