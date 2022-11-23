import math


# -- Recebe os valores para poder fazer a conta -- #
print("="*20)
a = int(input('Qual o valor de a? '))
b = int(input('Qual o valor de b? '))
c = int(input('Qual o valor de c? '))
# ------------------------------------------------ #

# -- Contas são feitas aqui -- #
D = float(((b)*(b)-4*a*c))
Yv = float(-D/(4*a))
Xv = float(-b/(2*a))

if D > 0:
    X1 = float((-b + math.sqrt(D))/(2*a))
    X2 = float((-b - math.sqrt(D))/(2*a))

if D == 0:
    X = float((-b/(2*a)))

x1: int = -2
x2: int = -1
x3: int = 0
x4: int = 1
x5: int = 2

y1: float = ((a)*(x1)**2+(b)*x1+(c))
y2: float = ((a)*(x2)**2+(b)*x2+(c))
y3: float = ((a)*(x3)**2+(b)*x3+(c))
y4: float = ((a)*(x4)**2+(b)*x4+(c))
y5: float = ((a)*(x5)**2+(b)*x5+(c))

# ---------------------------- #
if a > 0:
    str_a= f'{a}x²'
elif a == 0:
    str_a = ''
else: 
    str_a = f'{a}x²'
if b > 0:
    str_b = f'+{b}x'
elif b == 0:
    str_b = ''
else: 
    str_b = f'{b}x'
if c > 0:
    str_c = f'+{c}'
elif c == 0: 
    str_c = ''
else: 
    str_c = c
    
print("="*20)
print(f'{str_a}{str_b}{str_c}')
print("="*20)


# -- Imprime o resultado das contas -- #
print("D = ", D)
if D > 0:
    print("X1 =", X1)
    print("X2 =", X2)
if D == 0: 
    print(f'X = {X}')
if D < 0: 
    print('Delta é negativo, não existem raizes reais')
print(f"Yv = {Yv}")
print(f'Xv = {Xv}')

print("="*20) 

print ("   X  |  Y   ")
print ("------|------")
print (f"  -2  |  {y1}  ")
print (f"  -1  |  {y2}  ")
print (f"   0  |  {y3}  ")
print (f"   1  |  {y4}  ")
print (f"   2  |  {y5}  ")

print("="*20)

# ------------------------------------ #
