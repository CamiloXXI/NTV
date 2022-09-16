numero = 0;
empanada = {}
listaEmpanadas = []
centinela = 0
while(numero != 3):
    print("***Menú***")
    print("*** 1 Crear Empanada ***\n*** 2 Mostrar Empanadas ***\n*** 3 Salir ***")
    numero = int(input("Ingresa opción."))
    if(numero == 1):
        empanada['NombreEmpanada'] = input("Cuál es el nombre de la empanada: ")
        empanada['Ingrediente1'] = input("Cuál es el ingrediente 1 de la empanada: ")
        empanada['Ingrediente2'] = input("Cuál es el ingrediente 2 de la empanada: ")
        empanada['Ingrediente3'] = input("Cuál es el ingrediente 3 de la empanada: ")
        empanada['PrecioFabricacion'] = int(input("Cuál es el precio de fabricación de la empanada: "))
        empanada['PrecioVenta'] = int(input("Cuál es el precio de venta para la empanada: "))
        listaEmpanadas.extend(empanada)
        centinela+=1
    if(numero == 2):
        for i in listaEmpanadas:
            for clave,valor in empanada.items():
                print(clave, " : ", valor)

        
#Agregar buscador, eliminar empanada
        

 