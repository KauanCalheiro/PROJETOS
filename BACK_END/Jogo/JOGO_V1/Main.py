import random

n1 = int
n2 = int
n3 = int

n1 = random.randint(1, 4)
n2 = random.randint(1, 4)
n3 = random.randint(1, 4)
#print(f'({n1}, {n2}, {n3})') -- retorna valor sorteado

r1=int
r2=int
r3=int

sair = int (0)
score = int (0)

r = [r1, r2, r3]
n = [n1, n2, n3]

print ('Sim - 1')
print ('Não - 2')
jogar = int (input('Deseja jogar? '))

print(' ')
print('Quando desejar sair, digite "0" na entrada dos números.')
print(' ')

if (jogar == 1):
    while (r != n) or (sair == 2):
        sair=0 
        x=0
#----------------------------------------------------------------#                
        r1 = int(input('1º número: '))
        
        while r1 == 0:
            print(' ')
            sair = print('Sim - 1'), print('Não - 2')
            sair = int (input('Deseja sair? '))
            print(' ')
            if(sair == 1):
                print(' ')
                print('Obrigado por jogar ^-^')
                print (f'Seu score final foi de: {score}')
                print(' ')
                score= score*0
                exit()
            if(sair == 2):
                r1 = int(input('1º número: '))

        while (r1 > 4):
            print ("Valor inválido")
            r1 = int(input('1º número: '))
#----------------------------------------------------------------#
        r2 = int(input('2º número: '))
        
        while r2 ==0:
            print(' ')
            sair = print('Sim - 1'), print('Não - 2')
            sair = int (input('Deseja sair? '))
            print(' ')
            if(sair == 1):
                print(' ')
                print('Obrigado por jogar ^-^')
                print (f'Seu score final foi de: {score}')
                print(' ')
                score= score*0
                exit()
            if(sair == 2):
                print(f'1º número: {r1}')
                r2 = int(input('2º número: '))
                
        while (r2 > 4):
            print ("Valor inválido")
            r2 = int(input('2º número: '))
#----------------------------------------------------------------#
        r3 = int(input('3º número: '))
   
        while r3 == 0:
            print(' ')
            sair = print('Sim - 1'), print('Não - 2')
            sair = int (input('Deseja sair? '))
            print(' ')
            if(sair == 1):
                print(' ')
                print('Obrigado por jogar ^-^')
                print (f'Seu score final foi de: {score}')
                print(' ')
                score= score*0
                exit()
            if(sair == 2):
                print(f'1º número: {r1}')
                print(f'2º número: {r2}')
                r3 = int(input('3º número: '))
                
        while (r3 >4):
            print ("Valor inválido")
            r3 = int(input('3º número: '))
#----------------------------------------------------------------#
        r = [r1, r2, r3]     
        if (r1 == n1):
            x=x+1
        else:
            x=x+0           
        if (r2== n2):
            x=x+1    
        else:
            x=x+0            
        if (r3 == n3):
            x=x+1
        else:
            x=x+0
            
            
        if(r != n):
            print(' ')
            print(f'({r1}, {r2}, {r3})       Você acertou {x}')
            print(' ')
            x=0*x
                 
        if (r == n):
            score = score + 1
            print(' ')
            print(f'Parabéns a sequencia era: ({n1}, {n2}, {n3}) ')
            print(' ')
            sair = print('Sim - 1'), print('Não - 2')
            sair = int (input('Deseja jogar novamente? '))
            print(' ')
                
            if(sair == 2):
                print(' ')
                print('Obrigado por jogar ^-^')
                print (f'Seu score final foi de: {score}')
                print(' ')
                score= score*0
                exit()
            if(sair == 1):
                n1 = random.randint(1, 4)
                n2 = random.randint(1, 4)
                n3 = random.randint(1, 4)
                n = [n1, n2, n3]
                #print(f'({n1}, {n2}, {n3})') -- retorna valor sorteado   

if (jogar == 2):
    exit()