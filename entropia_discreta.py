###########################################
# Author: DanMat27
# Date: 29/05/2020
# File: entropia_discreta.py
# Description:
#  ENTROPIAS DE VARIABLES DISCRETAS
#  Calcula:
#  H(X) = - sum_i=1^n (p_i)*(log_2(p_i))
###########################################
import math 

print("#################################")
print("Introduzca los siguientes valores")
valores = int(input("Numero de variables: "))
i = 1 #Contador de variables
entropia = 0
while i<=valores:
    p = float(input("p_" + str(i) + ": ")) 
    i += 1
    if p==0:
        continue
    entropia += p*math.log(p,2)

entropia = -(entropia)
print("ENTROPIA = " + str(entropia)) 
print("#################################")