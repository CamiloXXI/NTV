#Función lambda
areaT = lambda base, altura: (base * altura) / 2

#Reto 1
numeroPar = lambda numero: print("Es par") if numero % 2 == 0 else print("Es impar")

numeroPar(2)


#Reto 2
mi_lista = [18, -3, 5, 0, -1, 12]
lista_nueva = list(filter(lambda numero: (numero > 10), mi_lista))
print(lista_nueva) # [18, 12]

#Reto 3


#Reto 4
suma = lambda numero1, numero2: (numero1 + numero2)

#Reto 5
multiplica = lambda numero: (numero * 100)