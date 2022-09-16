#Reto 1 

'''
El valle de aburra afronta altas temperaturas año tras año, Cree una que permita calcular la temperatura media de la tierra partir de recibir 20 datos diarios de temperatura.
'''

'''def temperaturaPromedioMedellin():
    acumulador = 0
    promedio = 0
    listaTemperatura = []
    for i in range(0, 20, 1):
        temperaturaHoy = int(input("Digita la temperatura de hoy:  "))
        listaTemperatura.append(temperaturaHoy)
    for i in listaTemperatura:
        acumulador = acumulador + i
        print(i)
    promedio = acumulador / 20
    print(promedio)

temperaturaPromedioMedellin()'''

#Reto 2
'''
Crea una función  que reciba una lista con valores numéricos y devuelva el valor máximo y el mínimo ingresados
'''
'''def min_max(tamagnoLista):
    listaNumeros = []
    for i in range(0, tamagnoLista, 1):
        valorIngresado = int(input("Digita el número a guardar en la lista:  "))
        listaNumeros.append(valorIngresado)

    valorMinimo = listaNumeros[0]
    valorMaximo = listaNumeros[0]

    for i in range(1, len(listaNumeros), 1):
        if(listaNumeros[i] > valorMaximo):
            valorMaximo = listaNumeros[i]
        elif(i < valorMinimo):
            valorMinimo = i

    print(f"El valor mínimo es {valorMinimo} y el valor máximo es {valorMaximo}")

tamagnoLista = 4
min_max(tamagnoLista)'''

#Reto 3

from ast import Return


def login():
    intentos = 0
    usuario = ""
    contraseña = ""
    correcto = False
    while(usuario != "admin"):
        usuario = input("Ingrese el nombre  ")
        if(usuario == "admin"):
            correcto = True
            break
        print("Usuario incorrecto.")
        intentos+=1
        print(f"Intento número {intentos}")

    while(contraseña != "admin12*"):
        contraseña = input("Digita contraseña:  ")
        if(contraseña == "admin12*"):
            correcto = True
            break
        print("Contraseña incorrecta.")
        intentos+=1
        print(f"Intento número {intentos}")

    print(f"{correcto} Número de intentos realizados {intentos}")

login()



#Reto 4

'''Escriba un programa que pida el ancho y largo de un rectángulo y permita calcular:
-Área
-Perímetro
-Graficar el rectángulo con *'''

'''def rectangulo(ancho, largo):
    asterisco = "*"
    for i in range(0, 1, 1):
        print("\n")
        for n in range(0, largo, 1):
            print(f"{asterisco * ancho}")

ancho = 5
largo = 3
rectangulo(ancho, largo)'''