#Listas
nombres = ["Camilo", "Sara", "Anthony"]

nombres.append("Isis")
nombres.insert(1, "Apolo")

for nombre in nombres:
    print(nombre)

#Tupla
tuplas = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for numero in tuplas:
    print(numero)


#Diccionario

diccionario = {
    'nombre': 'Camilo', #Item
    'apellido': 'Usuga', #Item
    'edad': 23, #Item
    'quiereHamburguesa': True, #Item
    'nacimiento': '2022-05-12' #Item
}

print(diccionario)
#Recorriendo diccionario
for clave,valor in diccionario.items():
    print(clave, valor)