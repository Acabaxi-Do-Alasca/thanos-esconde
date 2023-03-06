import random, os  

modoJogo = int(input("1-Você escolhe a qtde\n2-PC escolhe\nR:"))
if modoJogo == 1:
    narvores = int(input("Informe a qtde de árvores: "))
else:
    narvores = 50

esconde = random.randrange (0,narvores)

dificuldade = int(input(" 1-Facil \n 2-Medio \n 3-Dificil \n R: "))
acertou = False

if dificuldade == 1:
    tentativas = 15
elif dificuldade == 2:
    tentativas = 10
else:
    tentativas = 5

for x in range (0, tentativas) :
    print("Você tem " + str(x + 1) + " de " + str(tentativas) + " tentativas")

    nt = int (input("Informe seu numero: "))
    if nt > esconde:
        print("Esta mais a esquerda")
    elif nt < esconde: 
        print("Esta mais para a direita")
    else: 
        acertou = True
        break

if acertou == False:
    print("Você perdeu ele está na posição " + str(esconde))
else:
    print("Você o achou")

os.system("pause")