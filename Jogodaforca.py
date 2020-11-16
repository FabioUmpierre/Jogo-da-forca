import pandas as pd
df = pd.read_excel('excel.xlsx')
animal = 'animais'
objeto = 'objetos'
natural = 'natureza'
Lista = [animal,objeto,natural]

def Tenta_Acertar(p):
    if p == Palavra_Escolhida:
        print("Parabéns, você acertou a palavra!")
    else:
        print('Que pena, você errou, a palavra era: ' , Palavra_Escolhida)


Acabou = False
Palavra = []
Letras_Acerto = []
Letras_Erro = []
continua = 1

Chance = 4
Tentativa = 0
from random import randint

cont = randint(0,2)
categoria = Lista[cont]

palavra_aleatoria = randint(0,19)


Palavra_Escolhida = df[categoria][palavra_aleatoria]
z = []
x = len(Palavra_Escolhida)

Palavra_Oculta = []



for i in range(0,x):
    z.append(Palavra_Escolhida[i:i+1])
    Palavra_Oculta.append('-')


if continua == 1:
 while Acabou == False:
     if Palavra == Palavra_Escolhida :
         print("Você acertou a palavra, parabens!")
         continua = int(input("Deseja jogar outra vez? 1 para sim e 2 para nao: "))
     if continua != 1:
         Acabou = True
         break
     if Chance == 1:
         Acabou = True
     Letra = input('Digite uma letra: ').lower()
     while Letra in Letras_Acerto or Letra in Letras_Erro:
         Letra = input('Você já tentou essa letra, digite uma nova: ').lower()

     if Letra in z:
         Letras_Acerto.append(Letra)
     else :
         Letras_Erro.append(Letra)
         Chance -= 1

     print('Letras que o jogador jogou e acertou: ' ,Letras_Acerto,'---', end = ' ')
     print('Letras que o jogador jogou e errou: ', Letras_Erro)
     for i in range(0,x):
         if Letra == z[i]:
             Palavra_Oculta[i] = Letra
         for i in range(0, x):
             Palavra = ''.join(Palavra_Oculta)
     print('Palavra: ' ,Palavra)
     if Chance > 0:
      print('Voce ainda tem', Chance, 'Chances')
     else:
         print("Acabaram suas chances")



 if Palavra != Palavra_Escolhida:
     Tentativa = input("Tente acertar a palavra: ").lower()
     Tenta_Acertar(Tentativa)






















