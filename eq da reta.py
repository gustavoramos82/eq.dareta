from fractions import Fraction
from termcolor import colored
from matplotlib import pyplot as plt 

print(colored('-=-'*20,'yellow'))
print(colored('Digite duas coordenadas e digo a equação da reta que passa por elas',"green"))
print(colored('-=-'*20,'yellow'))

x1 = float(input('Valor do x da primeira coordenada:'))
y1 = float(input('Valor do y da primeira coordenada:'))

x2 = float(input('Valor do x da segunda coordenada:'))
y2 = float(input('Valor do y da segunda coordenada:'))

if x1 == x2 and y1 == y2:
    print(colored('Você repetiu as coordenadas, não se pode definir uma equação da reta por uma apenas uma coordenada.','red'))
    print(colored('Tente novamente colocando 2 coordenadas diferentes.','red'))

if x2-x1 == 0:
    print(colored('A diferença entre esses dois é igual a zero, não se pode efetuar','red'))
    print(colored('Tente novamente.','red'))

tg = (y2-y1)/(x2-x1)
cl = -tg*x1+y1

if cl > 0 :
    print(colored('A equação da reta é y= {}x + {}'.format(Fraction(tg),Fraction(cl)),'cyan'))
elif cl == 0:
    print(colored('A equação da reta é y = {}x'.format(Fraction(tg)),'cyan'))
else:
    print(colored('A equação da reta é y = {}x {}'.format(Fraction(tg),Fraction(cl)),'cyan'))

print('podemos tirar mais informações dessa equação da reta...')

if tg > 0:
    print(colored('Esta é uma reta crescente','blue'))
else:
    print(colored('Esta é uma reta descrescente','blue'))

plt.plot([0,1,2,3,4],[cl,tg+cl,2*tg+cl,3*tg+cl,4*tg+cl])
plt.show()