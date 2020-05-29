#########################################################################################
# Author: DanMat27
# Date: 29/05/2020
# File: entropia_condicional.py
# Description:
#  ENTROPIAS CONDICIONALES
#  Calcula:
#   H(Y|X) = sum_i=1^n (p_i)*H(p_cond_i,q_cond_i)
#  Donde:
#   p_i = Probabilidad P[X=x_i] en datos totales
#   == De los valores de X, cuantos son iguales a x_i sobre el total
#   p_cond_i = Probabilidad P[Y|X=x_i] condicionada por clase Y
#   == De los valores de X iguales a x_i, cuantos tienen la clase Y buena (1, sí...)
#   q_cond_i = 1 - p_cond_i
#   == De los valores de X iguales a x_i, cuantos tienen la clase Y contraria (0, No...)
#########################################################################################
import math 

print("#################################")
print("Introduzca los siguientes valores")
valores = int(input("Numero de valores de X: "))
i = 1 #Contador de valores de X
entropia = 0
while i<=valores:
    print("> Valor " + str(i) + " de " + str(valores) + " que tiene X")
    p = float(input(" p_" + str(i) + ": ")) # p_i
    p_cond = float(input(" p_cond_" + str(i) + ": ")) # p_cond_i
    q_cond = 1 - p_cond # q_cond_i
    if p==0 or p_cond==0 or q_cond==0:
        i += 1
        continue
    H = - (p_cond*(math.log(p_cond,2))) - (q_cond*(math.log(q_cond,2)))
    entropia += p*H
    i += 1

print("ENTROPIA = " + str(entropia)) 
print("#################################")