myDict = {'añy' : 2023,  'mes' : 2, 'dia' : 1, 'hora' : 19, 'minuto': 52, 'segundo' : 23}

#LONGITUD DICCIONARIO
print (len(myDict))

#VALORES DICCIONARIOS
print (myDict.values())

#ELIMINAMOS EL ULTIMO ITEM Y MOSTRAMOS LA LISTA FINAL
(myDict.popitem())
print(myDict)
