#----ADIVINHE O NÚMERO----#
import random 

numero_secreto = random.randint(1, 20)


print('Pensei erm um número do 1 a 20. Você tem 5 tentativas!')


for tentativa in range(1, 6):
    palpite = int(input('Seu palpite: '))
    
    if palpite < numero_secreto:
        print('Muito baixo. tente um número maior')
    elif palpite > numero_secreto:
        print('Muito alto. Tente um número menor')
    else:
        print(f'Acertou em {tentativa} tentativas!')
        break
else:
    print(f'Acabaram as tentativas! O número secreto era: {numero_secreto}')
        