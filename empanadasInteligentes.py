numero = 0;
empanada = {}
listaEmpanadas = []
centinela = 0
while(numero != 3):
    print("***Menú***")
    print("*** 1 Crear Empanada ***\n*** 2 Mostrar Empanada ***\n*** 3 Salir ***")
    numero = int(input("Ingresa opción."))
    if(numero == 1):
        empanada['NombreEmpanada'] = input("Cuál es el nombre de la empanada: ")
        empanada['Ingrediente1'] = input("Cuál es el ingrediente 1 de la empanada: ")
        empanada['Ingrediente2'] = input("Cuál es el ingrediente 2 de la empanada: ")
        empanada['Ingrediente3'] = input("Cuál es el ingrediente 3 de la empanada: ")
        empanada['PrecioFabricacion'] = int(input("Cuál es el precio de fabricación de la empanada: "))
        empanada['PrecioVenta'] = int(input("Cuál es el precio de venta para la empanada: "))
        listaEmpanadas.insert(centinela, empanada)
    centinela=+1
    if(numero == 2):
        for clave,valor in empanada.items():
            print(clave, valor)
        print(empanada)
        
#Agregar buscador, eliminar empanada
        

