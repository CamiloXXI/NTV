#Reto 1
'''Construir un programa para ir de compras a un supermercado que permita la construcción del siguiente menú:

Digitar 1 para recibir código, nombre y precio de un producto
Digitar 2 para mostrar los productos
Digitar 3 para buscar y editar producto por código
Digitar 4 para buscar y eliminar producto por código '''

'''listaSupermarket = []
compra = {}
opcion = 100

while(opcion != 0):
    print("     Menú       \nDigitar 1 para recibir código, nombre y precio de un producto\nDigitar 2 para mostrar los productos\nDigitar 3 para buscar y editar producto por código\nDigitar 4 para buscar y eliminar producto por código")
    opcion = int(input("Qué opción desea elegir?  "))

    if(opcion == 1):
        compra["codigo"] = int(input("Ingrese el código del producto:  "))
        compra["nombre"] = input("Ingrese el nombre del producto:  ")
        compra["precio"] = int(input("Ingrese el precio del producto:  "))
        listaSupermarket.append(compra)
    if(opcion == 2):
        for i in listaSupermarket:
            print(i)
    if(opcion == 3):
        buscarCodigo = int(input("Qué código deseas buscar?  "))
        for i in listaSupermarket:
            if(i["codigo"] == buscarCodigo):
                print(i)
                nombreNuevo = input("Ingrese el nuevo nombre del producto:  ")
                precioNuevo = int(input("Digita el nuevo precio del producto: "))
                i["nombre"] = nombreNuevo
                i["precio"] = precioNuevo
                print(listaSupermarket)
                break
    if(opcion == 4):
        buscarCodigo = int(input("Qué código deseas buscar?  "))
        for i in listaSupermarket:
            if(i["codigo"] == buscarCodigo):
                print(i)
                listaSupermarket.remove(i)
                print(listaSupermarket)'''

#Reto 2
'''
Construir un programa para calcular un programa CALCULADORA que permita calcular
SUMA
RESTA
MULTIPLICACIÓN
DIVISIÓN
'''

'''class MatematicaBasica:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def suma(self):
        return self.numero1 + self.numero2
    
    def resta(self):
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        return self.numero1 / self.numero2

operacionRealizar = 10
while(operacionRealizar != 0):
    print("     OPERACIONES      \n1-> SUMA\n2-> RESTA\n3-> MULTIPLICACIÓN\n4-> DIVISIÓN\n0-> SALIR")
    operacionRealizar = int(input("Ingrese la operación que desea realizar:  "))
    if(operacionRealizar == 0):
        break
    numero1 = int(input("Ingrese el número 1:  "))
    numero2 = int(input("Ingrese el número 2:  "))
    operacion = MatematicaBasica(numero1, numero2)

    if(operacionRealizar == 1):
        print(operacion.suma())
    if(operacionRealizar == 2):
        print(operacion.resta())
    if(operacionRealizar == 3):
        print(operacion.multiplicacion())
    if(operacionRealizar == 4):
        print(operacion.division())'''


#RETO 3
'''
3. El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:

Almacenar información de un cliente (nombre,apellido,cedula)
Almacenar información de la cuenta (numeroCuenta, saldo)
Se debe permitir consultar saldo en cualquier momento
Se debe permitir ingresar o retirar dinero  cuando se desee
'''
cliente = {}
cuenta = {}
usuarios = []
cuentas = []
opcion = 10

while(opcion != 0):
    print("     OPCIONES      \n1-> Almacenar información de un cliente (nombre,apellido,cedula)\n2-> Almacenar información de la cuenta (numeroCuenta, saldo)\n3-> Consultar Saldo\n4-> Ingresar o retirar efectivo.\n0-> SALIR ¡MUERTE A LOS LANNISTER! Excepto al gnomo.")
    opcion = int(input("Qué opción desea elegir?  "))
    if(opcion == 0):
        break
    if(opcion == 1):
        cliente["cedula"] = input("Ingrese el número de cédula:  ")
        cliente["nombre"] = input("Ingrese el nombre:  ")
        cliente["apellido"] = input("Ingrese el apellido:  ")
        usuarios.append(cliente)
    if(opcion == 2):
        cuenta["numeroCuenta"] = input("Ingrese el número de la cuenta:  ")
        cuenta["saldo"] = int(input("Ingrese el saldo de la cuenta:  "))
        cuentas.append(cuenta)
    if(opcion == 3):
        numeroCuenta = input("Ingrese el número de la cuenta:  ")
        for i in cuentas:
            if(i["numeroCuenta"] == numeroCuenta):
                print(f"\n\nSu saldo es ${i['saldo']} con el número de cuenta {i['numeroCuenta']}\n\n")
    if(opcion == 4):
        opcionSaldo = int(input("Si desea retirar digite 1 y para ingresar efectivo digite 2  "))
        if(opcionSaldo == 1):
            numeroCuenta = input("Ingrese el número de la cuenta:  ")
            for i in cuentas:
                if(i["numeroCuenta"] == numeroCuenta):
                    print(f"\nSu saldo es de {i['saldo']}\n")
                    retirar = int(input("Cuánto desea retirar:  "))
                    i["saldo"] -= retirar
                    print(f"Su saldo actual queda en {i['saldo']}")
        if(opcionSaldo == 2):
            numeroCuenta = input("Ingrese el número de la cuenta:  ")
            for i in cuentas:
                if(i["numeroCuenta"] == numeroCuenta):
                    print(f"\nSu saldo es de {i['saldo']}\n")
                    ingresar = int(input("Cuánto desea ingresar:  "))
                    i["saldo"] += ingresar
                    print(f"\nSu saldo actual queda en {i['saldo']}\n")
