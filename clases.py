class Cliente:

    def __init__(this, nombre, apellido, cedula):
        this.nombre = nombre
        this.apellido = apellido
        this.cedula = cedula

class Cuenta:
    def __init__(self, numeroCuenta, saldo):
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
#from clases import Personaje 
'''
Para usar una clase debo crear una instancia
Un objeto es una variable
'''

clientes = []
cuentas = []