from math import fabs


nombres = ["Camilo", "Anthony", "Isis", "Ferxxo"]

for nombre in nombres:
    print(nombre)

#Longitud
print(len(nombres))
#Insertar
nombres.append("Nieve")
#Insertar en índice específico
nombres.insert(2, "XXI")
print(len(nombres))
print(nombres)
#Remover elemento
nombres.remove("Nieve")
#Remover elemento por índice
del nombres[0]
#Limpiar lista
nombres.clear()
print(nombres)

print("Retos\n\n\n")
'''
** Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7

** Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario

** Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados

** Leer 20 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso

'''

#Reto1
'''tamagnoLista = int(input("¿Cúal es el tamaño de la lista?  "))
multiplosSiete = []
for i in range(0, tamagnoLista, 1):
    multiplosSiete.append(i*7)
    print(multiplosSiete[i])
'''
#Reto2
'''
tamagnoLista = int(input("¿Cúal es el tamaño de la lista?  "))
numerosRecibidos = []
for i in range(0, tamagnoLista, 1):
    numeroEntregado = int(input("¿Qué numero desea ingresar?  "))
    numerosRecibidos.append(numeroEntregado)

print(numerosRecibidos)
'''
#Reto3
'''
listaCiudades = ["Medellín", "Bogotá", "Tunja", "Bucaramanga", "Ibagué", "Cali", "Pereira", "Montería"]

for i in range(7, -1, -1):
    print(listaCiudades[i])
'''
#Reto4
numeros = []
for i in range(0, 3, 1):
    numeroIngresado = int(input("Ingrese número  "))
    numeros.append(numeroIngresado)

numeroBuscar = int(input("Ingrese el número que desea hallar:  "))
verifica = None

for i in range(0, len(numeros), 1):
    verifica = numeros[i] == numeroBuscar
    if(verifica):
        verifica = False
        print(f"El número ingresado se halla en la lista. Tu número es {numeroBuscar}")
    
if(verifica == False):
    print(f"El número ingresado no se halla en la lista. Tu número es {numeroBuscar}")

