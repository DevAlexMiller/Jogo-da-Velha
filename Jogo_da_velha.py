#Jogo_da_velha
'''
FPOO
Autor: Alex Miller
'''
def tabela():
    if jogo[0][0]==0:
        jogo[0][0]='*'
    if jogo[0][1]==1:
        jogo[0][1]='*'
    if jogo[0][2]==2:
        jogo[0][2]='*'
    if jogo[1][0]==3:
        jogo[1][0]='*'
    if jogo[1][1]==4:
        jogo[1][1]='*'
    if jogo[1][2]==5:
        jogo[1][2]='*'
    if jogo[2][0]==6:
        jogo[2][0]='*'
    if jogo[2][1]==7:
        jogo[2][1]='*'
    if jogo[2][2]==8:
        jogo[2][2]='*'
    print(f"Finalizado! Jogador {a} venceu!")
    tabelaGeral()
def tabelaGeral():
    print(jogo[0])
    print(jogo[1])
    print(jogo[2])
def finalizar():
    if jogo[0][0]==jogo[0][1] and jogo[0][0]==jogo[0][2]:
        tabela()
        y=77
        return y 
    elif jogo[1][0]==jogo[1][1] and jogo[1][0]==jogo[1][2]:
        tabela()
        y=77
        return y 
    elif jogo[2][0]==jogo[2][1] and jogo[2][0]==jogo[2][2]:
         tabela()
         y=77
         return y 
    elif jogo[0][0]==jogo[1][0] and jogo[0][0]==jogo[2][0]:
         tabela()
         y=77
         return y 
    elif jogo[0][1]==jogo[1][1] and jogo[0][1]==jogo[2][1]:
         tabela()
         y=77
         return y 
    elif jogo[0][2]==jogo[1][2] and jogo[0][2]==jogo[2][2]:
         tabela()
         y=77
         return y 
    elif jogo[0][0]==jogo[1][1] and jogo[0][0]==jogo[2][2]:
         tabela()
         y=77
         return y 
    elif jogo[0][2]==jogo[1][1] and jogo[0][2]==jogo[2][0]:
         tabela()
         y=77
         return y 
def jogadas():
        if jogada==jogo[0][0]:
            jogo[0][0]=a
        elif jogada==jogo[0][1]:
            jogo[0][1]=a
        elif jogada==jogo[0][2]:
            jogo[0][2]=a
        elif jogada==jogo[1][0]:
            jogo[1][0]=a
        elif jogada==jogo[1][1]:
            jogo[1][1]=a
        elif jogada==jogo[1][2]:
            jogo[1][2]=a
        elif jogada==jogo[2][0]:
            jogo[2][0]=a
        elif jogada==jogo[2][1]:
            jogo[2][1]=a
        elif jogada==jogo[2][2]:
            jogo[2][2]=a
        tabelaGeral()
def recomeco():
     x=(input("Deseja começar de novo? [s] [n] "))
     if x=='s':
         x=0
         return x
     if x=='n':
         print("Jogo finalizado!")
         x=77
         return x
a='x'    
x=0
y=0
anterior=10
jogo=[[0,1,2],[3,4,5],[6,7,8]]
print("JOGO DA VELHA")
print("--------------------------------------------")
tabelaGeral()
while y==0:
    while x<9:
        try:  
            print("--------------------------------------------")
            a='X'
            jogada=int(input(f"1°Jogador({a})-Qual a posição da jogada? "))
            if jogada==anterior:
                print("Você não pode inserir dois valores para o mesmo espaço")
                break
            anterior=jogada
            f=jogadas()
            d=finalizar()
            x=x+1
            if x>=9:
                print("Jogo finalizado! Velha")
                break 
            if d==77 or f==77:
                break
            a='O'
            jogada=int(input(f"2°Jogador({a})-Qual a posição da jogada? "))
            if jogada==anterior:
                print("Você não pode inserir dois valores para o mesmo espaço!")
                break
            anterior=jogada
            f=jogadas()   
            d=finalizar()
            x=x+1
            if x>=9:
                print("Jogo finalizado! Velha")
                break
            if d==77 or f==77:
                break
        except:
            break
    y=recomeco()
    jogo=[[0,1,2],[3,4,5],[6,7,8]]
    tabelaGeral()
    x=0
