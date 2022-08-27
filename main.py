from math import sqrt


print("Clase 1")

'''
    Comentarios
    Los nombres de variables deben iniciar en minúscula, los de las clases en mayúscula.
'''

#Comentarios de GIT
'''
    GIT INIT ---> Inicializa la Rama
    GIT ADD ---> Agrega los nuevos cambios
    GIT STATUS ---> Muestra el estatus de los commits
    GIT COMMIT ---> Toma la foto
    Regla de clase al darle mensaje al Commit ---> NTV1 (El número varía por la clase)
    GIT LOG ---> Muestra los commits.
    GIT REMOTE ADD origin https://github.com/usuario/repositorio.git ---> Añadir repositorio en remoto.
    GIT PUSH -U ORIGIN MASTER ---> La primera vez que vinculamos el repositorio remoto con el local.
    GIT PULL ---> Para descargar los cambios del repositorio remoto al local.
    GIT CLONE (URL) ---> Clonar repositorio al local.
    GIT COMMIT --AMEND -M "" ---> Renombrando commit
    GIT CONFIG --GLOBAL --UNSET CREDENTIAL.HELPER 
    GIT CONFIG --UNSET CREDENTIAL.HELPER 
'''

print("Clase 2 NTV")

'''
    Convensiones ---> Estructurar adecuadamente los archivos.
    .gitignore ---> Archivo de configuración. Especificar las carpertas o archivos que no voy a versionar.
'''

#Entradas del problema.
#En python siempre se le debe dar valor a una variable;
#Para dejarla sin un valor agregamos la palabra none.
'''
numero1 =  None
numero2 = int(input("Digite el número 2: "))
numero3 = int(input("Digite el número 3: "))
#numero3 = 80
print(f'El número 2 es {numero2}')
print(f'El número 3 es {numero3}')
suma = numero2 + numero3
print(f'La suma es {suma}')
'''
'''
ciudad = "Medellín"
print(f'Tu ciudad es {ciudad}')
print(numero1)
print(numero2)
print(numero3)
print(numero3 == numero1)
nombre = input("Ingresa nombre: ")
print(f'Su nombre es {nombre}')
'''

#Retos
print("Clase 3 NTV")

print("Retos")

numero = 1
suma = 0
while(numero >= 0):
    numero = int(input("Digite un número entero positivo; uno negativo para salir: "))
    print(f'El número es {numero}')
    suma = suma + numero
    print(f'La suma es {suma}')

print("Has salido.")


#Menú

numero = 1

while (numero != 0):
    print(" 0 ---> Salida \n 1 ---> Encuentre si el número es múltiplo de 2 \n 2 ---> Encuentre la raiz cuadrada del número \n 3 ---> Sume 100 al número ingresado \n 4 ---> Eleve a la 2 el número ingresado.")

    numero = int (input("Qué opción elegirás: "))
    if(numero == 1):
        numeroMultiploDos = int(input("Ingrese el número a averiguar si es múltiplo de 2:  "))
        residuo = numeroMultiploDos % 2
        if(residuo == 0):
            print("Es múltiplo de 2.")
        else:
            print("No es múltiplo de 2.")

    if(numero == 2):
        numeroRaizCuadrada = int(input("Ingrese el número para saber su raiz cuadrada:  "))
        raizCuadrada = sqrt(numeroRaizCuadrada)
        print(f'La raiz cuadrada de {numeroRaizCuadrada} es {raizCuadrada}')

    if(numero == 3):
        numeroSumar = int(input("Ingrese el número al que desea sumarle 100:  "))
        numeroSumar = numeroSumar + 100
        print(f'El resultado es {numeroSumar}.')

    if(numero == 4):
        numeroElevar = int(input("Ingrese el número a elevar:  "))
        elevar = numeroElevar * 2
        print(f'El número a elevar que ingresaste fue {numeroElevar} y el resultado es {elevar}')


#Suma de 12 en 12

for i in range(0, 200, 12):
    print(i, end=", ")

print("\n")
#Pedir 20 números y contar cuántos fueron negativos y positivos.
numeroEntero = None
centinela = 0
contadorPositivos = 0
contadorNegativos = 0

while(centinela < 20):
    numero = int(input("Ingrese un número:  "))
    if(numero > 0):
        contadorPositivos += 1
    else:
        contadorNegativos += 1
    
    centinela+=1

print(f'Números negativos ingresados {contadorNegativos}. Números positivos ingresados {contadorPositivos}')

'''Clase 4'''

'''
# crear rama
git branch nombre-rama

# cambiar de rama
git checkout nombre-rama

# crear una rama y cambiarte a ella
git checkout -b rama

# eliminar rama
git branch -d nombre-rama

#eliminar rama (forzado)
git branch -D nombre-rama

# listar todas las ramas del repositorio
git branch

# lista ramas no fusionadas a la rama actual
git branch --no-merged

# lista ramas fusionadas a la rama actual
git branch --merged

# rebasar ramas
git checkout rama-secundaria
git rebase rama-principal

# nos cambiamos a la rama principal que quedará de la fusión
git checkout rama-principal

# ejecutamos el comando merge con la rama secundaria a fusionar
git merge rama-secundaria

git push origin --delete rama
'''

#Git
'''
Git reset --soft (ID del Commit)
'''