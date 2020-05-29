#ENTROPIAS DE VARIABLES BINARIAS
#Calcula:
# H(X) = - (p)*(log_2(p)) - (q)*(log_2(q))
#Donde:
# q = 1 - p
import math 

print("#################################")
print("Introduzca el siguiente valor")
p = float(input("p: ")) 
q = 1 - p

zero = False
if p==0 or q==0:
    zero = True

if zero:
    entropia = 0
else:
    entropia = - (p*(math.log(p,2))) - (q*(math.log(q,2)))

print("ENTROPIA = " + str(entropia)) 
print("#################################")
