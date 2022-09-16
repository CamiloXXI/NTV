miLista = ["Camilo", "Anthony"]
miDiccionario = {
    "España": "Madrid",
    "Colombia" : "Bogotá",
    "Francia" : "París",
    "UK" : "Londres",
    23: "Jordan",
    21 : "XXI",
    miLista[0] : "Usuga",
    miLista[1] : "Usuga",
    "Ingredientes" : {"Clave" : ["One", "Two", "Three"]}
}

miDiccionario["Brasil"] = "Error"
miDiccionario["Brasil"] = "Brasilia"
print(miDiccionario)
#Eliminar elemento
del miDiccionario["Brasil"]
print(miDiccionario)