# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
author:@Julio Cesar Froes de Oliveira

criar jogo da velha em python
author: @Vvendetta Julio

"""


board= [ [0,1,2],
        [3,4,5],
        [6,7,8] ]
    
def exibe():
    print(board[0])
    print(board[1])
    print(board[2])
    
def jogada():
    exibe()
    jogada = int(input("Digite o valor correspondente à sua jogada: "))
    return jogada
    
def definirjogadaX():
    jog = jogada()
    while jog <0 or jog > 8:
        print("Entrada inválida.")
        jog = jogada()
    if jog == 0:
        board[0].remove(0)
        board[0].insert(0,'X')
    elif jog == 1:
        board[0].remove(1)
        board[0].insert(1,'X')   
    elif jog == 2:
        board[0].remove(2)
        board[0].insert(2, 'X')
        
    elif jog == 3:
        board[1].remove(3)
        board[1].insert(0, 'X')
    elif jog == 4:
        board[1].remove(4)
        board[1].insert(1, 'X')
    elif jog == 5:
        board[1].remove(5)
        board[1].insert(2, 'X')
        
    elif jog == 6:
        board[2].remove(6)
        board[2].insert(0, 'X')
    elif jog == 7:
        board[2].remove(7)
        board[2].insert(1, 'X')
    elif jog == 8:
        board[2].remove(8)
        board[2].insert(2,'X')
    else:
        print("Entrada inválida!")
        
def definirjogadaO():
    jog = jogada()
    while jog <0 or jog > 8:
        print("Entrada inválida.")
        jog = jogada()
    while jog == str:
        print("Entrada inválida")
        jog = jogada()
    if jog == 0:
        board[0].remove(0)
        board[0].insert(0,'O')
    elif jog == 1:
        board[0].remove(1)
        board[0].insert(1,'O')   
    elif jog == 2:
        board[0].remove(2)
        board[0].insert(2, 'O')
        
    elif jog == 3:
        board[1].remove(3)
        board[1].insert(0, 'O')
    elif jog == 4:
        board[1].remove(4)
        board[1].insert(1, 'O')
    elif jog == 5:
        board[1].remove(5)
        board[1].insert(2, 'O')
        
    elif jog == 6:
        board[2].remove(6)
        board[2].insert(0, 'O')
    elif jog == 7:
        board[2].remove(7)
        board[2].insert(1, 'O')
    elif jog == 8:
        board[2].remove(8)
        board[2].insert(2,'O')
    else:
        print("Entrada inválida!")
        
    
    
def jogo():
    
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print("Jogador 1 venceu!")
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        print("Jogador 2 venceu!")
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print("Jogador 1 venceu!")
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        print("Jogador 2 venceu!")
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print("Jogador 1 venceu!")
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        print("Jogador 2 venceu!")
    elif board[0][0] == 'X' and board[0][1] =='X' and board[0][2] == 'X':
        print("Jogador 1 venceu!")
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        print("Jogador 1 venceu!")
    elif board[0][0] == 'O' and board[0][1] =='O' and board[0][2] == 'O':
        print("Jogador 2 venceu!")
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        print("Jogador 2 venceu!")
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print("Jogador 1 venceu!")
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        print("Jogador 2 venceu!")
    elif  board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print("Jogador 1 venceu!")
    elif  board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        print("Jogador 2 venceu!")
    elif board[0][2]=='X' and board[1][1]=='X' and board[2][0] == 'X':
        print("Jogador 1 venceu!")
    elif board[0][2]=='O' and board[1][1]=='O' and board[2][0] == 'O':
        print("Jogador 2 venceu!")
    else:
        return False

def game():
    while jogo()==False:
        jogador1 = definirjogadaX()
        jogador2 = definirjogadaO()
    print("Fim de jogo")
    x = int(input("1 Para jogar novamente e 2 para sair: "))
    if x == 1:
        game()
    elif x == 2:
        pass
    else:
        print("Entrada inválida")
        x = int(input("1 Para jogar novamente e 2 para sair: "))
game()
