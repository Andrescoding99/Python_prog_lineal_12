"""Buscar un metodo en internet, que muestre en pantalla sin que yo haga nada "Presione una tecla para continuar" - palabra reservada

Reemplazar el valor de la poscion 1 (vista de progrmacion), por la palabra "Dato alterado"

El metodo remove trabaja con el valor no la posicion."""


"""Capture 5 nombres proporcionados por el usuario, utilizar vectores:
Mostrar en pantalla los datos almacenados y realice una pausa de tecla
De los siguientes registros, elimine el que se encuentre en la posición 2 (programacion)
Modifique el nombre almacenado en la posición 1 por: “Dato alterado”
Muestre nuevamente los registros y realice una pausa de tecla"""

import os


# Declarando el vector

vec = []

#Declarando el iterador

i = 0
j = 0

#Lectura de datos / llenado del vector

print("Bienvenido")

for i in range(5):
    vec.append(input("Favor ingresar el nombre {}: ".format(i+1)))

print("\nDatos a mostrar")

while j < len(vec):
    print(vec[j])
    j += 1
#Esto se hace, dado que hay una X cantidad de vectores, se imprimen los vectores uno por uno
# Se debe usar WHILE con el vec[x] para mostrar los datos de los vectores en forma natural 

os.system("pause")

j = 0

while j < len(vec):
    if j == 1:
        vec.remove(vec[j])
    if j == 0:
        vec[j] = "Dato alterado"
    j += 1

j = 0

while j < len(vec):
    print(vec[j])
    j += 1
    
os.system("pause")



