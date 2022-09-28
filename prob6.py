a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))
import math
def triunghi(a,b,c,d):
    m=''
    if (a+b>=c) and (c+b>=a) and (a+c>=b): 
        m='DA'
        p=(a+b+c)/2
        s='Area triunghilui-',math.sqrt(p*(p-a)*(p-b)*(p-c))
        per='Perimetrul triunghilui-',a+b+c
    elif(c+b>d) and (d+c>b) and (b+d>c): 
        m='DA'
        p=(d+b+c)/2
        s='Area triunghilui-',math.sqrt(p*(p-d)*(p-b)*(p-c))
        per='Perimetrul triunghilui-',d+b+c
    elif(a+c>d) and (a+d>c) and (d+c>a):
        m='DA'
        p=(a+d+c)/2
        s='Area triunghilui-',math.sqrt(p*(p-a)*(p-d)*(p-c))
        per='Perimetrul triunghilui-',a+d+c
    elif(a+b>d) and (a+d>b) and (b+d>a):
        m='DA'
        p=(a+b+d)/2
        s='Area triunghilui-',math.sqrt(p*(p-a)*(p-b)*(p-d))
        per='Perimetrul triunghilui-',a+b+d
    else:
        m='NU'
        s='area la un triunghi inexistent nu poate fi calculata'
        per='perimetru la un triunghi inexistent nu poate fi calculat'
    return m,s,per

print("Din numerele pot fi formate triungiurile-",triunghi(a,b,c,d))