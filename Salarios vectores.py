"""Llenar por usuario un vector de salarios:
Cantidad de determinada por el usuario
Mostrar los salarios, agrupados por cantidades con decimales y enteros
Mostrar en pantalla, cuál de los dos fue la moda
Mostrar la mayor cantidad ingresada
Mostrar la menor cantidad ingresada """


#Declarando variables

mayor = -99999999999999
menor = 99999999999999
moda = 0

# Declarando el vector

vec = []
vecE = [] #Este es el vector para enteros 
vecD = [] #Este es el vector para decimales 

#Declarando el iterador

i = 0
j = 0


# Lectura de datos / llenado del vector (lista)

print ("Bienvenido")

i = int(input("Ingrese la cantidad de salarios que quiere meter: "))
while i <= 0:
    print("\nHa ingresado un valor fuera del rango para la cantidad de salrios, intente otra vez")
    i = int(input("Ingrese la cantidad de salarios que quiere meter: "))
print("\nValor de salarios nuevo aceptado\n") 


for j in range(i):
    vec.append(float(input("Favor ingresar el salario {}: ".format(j+1)))) 

print("\nSalarios ingresados")
print()

i = 0 #Reinicializar el iterador

while i < len(vec):
    print(vec[i])
    i += 1

print("---------------------------------------------------------------------------------------")
print("Salarios agrupados")

i = 0 #Reinicializar el iterador

while i < len(vec):
    entero = int(vec[i])
    if entero == vec[i]:
        vecE.append(vec[i])
    else:
        vecD.append(vec[i])
    
    i += 1

i = 0 #Reinicializar el iterador

print("\nSalarios enteros")

while i < len(vecE):
    print(vecE[i])
    i += 1

i = 0 #Reinicializar el iterador

print("\nSalarios decimales")

while i < len(vecD):
    print(vecD[i])
    i += 1

print("---------------------------------------------------------------------------------------")
print("Mayor salario")

j = 0 #Reiniciar el iterador

while j < len(vec):
    if vec[j] > mayor:
        mayor = vec[j]
    j += 1

print("El salario mayor es: {}".format(mayor))

print("---------------------------------------------------------------------------------------")
print("Menor salario")

i = 0 #Reiniciar el iterador

while i < len(vec):
    if vec[i] < menor:
        menor = vec[i]
    i += 1

print("El salario menor es: {}".format(menor))

print("---------------------------------------------------------------------------------------")
print("Calculo de la moda")

if len(vecE) > len(vecD):
    print("El grupo que se repetio más fue: el grupo de los enteros")
elif len(vecE) == len(vecD):
    print("Los dos grupos se repetieron las mismas veces")
else:
    print("El grupo que se repetio más fue: el grupo de los decimales")