import numpy as np

jogadas = 0
matriz = np.array([str(i) for i in range(1, 10)]).reshape(3, 3)


def checar_vitoria(matriz, jogador):
    for i in range(3):
        if all(matriz[i, j] == jogador for j in range(3)) or all(matriz[j, i] == jogador for j in range(3)):
            return True
    
    if all(matriz[i, i] == jogador for i in range(3)) or all(matriz[i, 2 - i] == jogador for i in range(3)):
        return True
    
    return False


for linha in matriz:
    print("  ".join(linha))
print(" ")


while True:


    if (checar_vitoria(matriz, 'X')) or (checar_vitoria(matriz, 'O')):
        break
    elif(jogadas >= 7):
        print("Jogo finalizado! Deu velha!")
        break

    while True:
        jogadaX = int(input("Vai jogar [X] em qual posição? "))
        print('')

        if(1 <= jogadaX <= 9 ):
            linha = (jogadaX - 1) // 3
            coluna = (jogadaX - 1) % 3

            matriz[linha, coluna] = 'X'

            jogadas += 1

            for linha in matriz:
                print("  ".join(linha))
            
            print(' ')
            break
        else:
            print("Digite o valor correto!")
            break
    
    
    if checar_vitoria(matriz, 'X'):
        print("Jogo finalizado. ")
        print("O jogador [X] ganhou! ")
        break
    
    

        
    while True:
        jogadaO = int(input("Vai jogar [O] em qual posição? "))

        if(1 <= jogadaO <= 9):
            linha = (jogadaO - 1) // 3
            coluna = (jogadaO - 1) % 3

            matriz[linha, coluna] = 'O'

            jogadas += 1

            for linha in matriz:
                print("  ".join(linha))

            print(" ")
            break

        else:
            print("Digite o valor correto!")
            break

    
    if checar_vitoria(matriz, 'O'):
        print("Jogo finalizado. ")
        print("O jogador [O] ganhou! ")
        break


    

    
    


            
