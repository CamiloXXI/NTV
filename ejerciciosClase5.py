#Reto 1
'''tupla=(50, 45, 20, 30, 40, 87)
listaNumeros = list(tupla)
#print(tupla[0])
for i in listaNumeros:
    if(i <= 40):
        listaNumeros.remove(i)
print(listaNumeros)'''

    
#Reto 2

tupla=(50,45,20,30,40,87)
listaNumeros = list(tupla)

for i in listaNumeros:
    if(not i % 2 == 0):
        listaNumeros.remove(i)
print(listaNumeros)