#DISTANCIA EUCLIDE AL CUADRADO (d^2)
#Calcula:
# d^2 = sum_i=1^n (x_i - test_i)^2
#Donde:
# x_i = Valor del atributo i de una tupla x 
# test_i = Valor del atributo i del test que se compara con x
import math 

print("#################################")
print("Introduzca los siguientes valores")
atributos = int(input("Numero de atributos a comparar: "))
i = 1 #Contador de atributos
d = 0
while i<=atributos:
    print("> Atributo " + str(i) + " de " + str(atributos))
    x = int(input(" x_" + str(i) + ": ")) 
    test = int(input(" test_" + str(i) + ": ")) 
    dif = (x - test)
    d += dif*dif
    i += 1

print("d^2 = " + str(d)) 
print("#################################")
