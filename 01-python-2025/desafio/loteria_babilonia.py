# Construa um programa que realize um sorteio de um número entre 1 e 15.
#O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
#Caso o usuário acerte, dê os parabéns

from random import randint

numero_sorteado = randint(1, 15)

tentativas = 3
palpite = 0

for i in range(tentativas, 0, -1):
    print('========= SORTEIO DA BABILÔNIA =========')
    print(f'VIDAS: {i}')
    print('========================================')
    chute = int(input('Digite o número sorteado: '))

    if(chute == numero_sorteado):
        palpite = 1
        break
    
    if(chute > numero_sorteado):
        print('O número sorteado é menor!')
    else:
        print('O número sorteado é maior')
        
print(f'O número sorteado era: {numero_sorteado}')
if(palpite == 1):
    print('PARABÉNS, VOCÊ ACERTOU')
else:
    print('BURRO DEMAIS! FDP')