# Calculadoras
#### Calculadoras variadas en lenguaje Python: 

1. Entropía de variables binarias (entropia_binaria.py)
2. Entropía de variables discretas (entropia_discreta.py)
3. Entropía condicional (entropia_condicional.py)
4. Distancia euclídea al cuadrado (distancia_euclidea_2.py)

Todos estos programas se deben ejecutar con Python3.

#### - Descripción:

entropia_binaria.py
-------------------
Al ejecutarlo, se debe introducir por teclado el valor de p.  
Calcula: H(X) = - (p)*(log_2(p)) - (q)*(log_2(q))  
Donde: q = 1 - p


entropia_discreta.py
--------------------
Al ejecutarlo, se debe indicar el número de variables a tener en cuenta y, luego, introducir
su valor de p (p_i) uno a uno por teclado.  
Calcula: H(X) = - sum_i=1^n (p_i)*(log_2(p_i))  


entropia_condicional.py
-----------------------
Al ejecutarlo, se debe indicar el número de atributos que se tendrán en cuenta y, luego, introducir
sus valores de p (p_i) y p condicionada (p_cond_i).  
Calcula: H(Y|X) = sum_i=1^n (p_i)*H(p_cond_i,q_cond_i)  
Donde: p_i = Probabilidad P[X=x_i] en datos totales  
       == De los valores de X, cuantos son iguales a x_i sobre el total  
       p_cond_i = Probabilidad P[Y|X=x_i] condicionada por clase Y  
       == De los valores de X iguales a x_i, cuantos tienen la clase Y buena (1, sí...)  
       q_cond_i = 1 - p_cond_i  
       == De los valores de X iguales a x_i, cuantos tienen la clase Y contraria (0, No...)  

distancia_euclidea_2.py
-----------------------
Al ejecutarlo, se debe indicar el número de atributos a comparar en el cálculo de la distancia, y
luego, introducir cada uno de sus valores enfrentando los valores de los atributos i de x (x_i) con
los valores i de test (test_i).  
Calcula: d^2 = sum_i=1^n (x_i - test_i)^2  
Donde: x_i = Valor del atributo i de una tupla x  
       test_i = Valor del atributo i del test que se compara con x  

  
-----------------------
*Este repositorio está abierto a incluir más tipos de calculadoras.*
