#imprima la cantidad de calorias de la fruta ingresada
#no importa si es mayusculas o minusculas
#no importa si el usuario pone en plural
#si no se encuentra el alimento devolver un mensaje "Por favor verifique"

frutas = {
    'Uva' : '20',
    'Manzana' : '45',
    'Durasno' : '10',
    'Sandia' : '5',
    'Papaya' : '8',
    'Kiwi' : '21',
    'Naranja' : '53'
}
#Primero le pedimos al usuario ingresar el nombre de una fruta

fruta = input("Por favor ingrese una fruta: ")

#Con el capitalize evitamos cualquier diferencia en cuanto a los nombrea

fruta = fruta.capitalize()
#buscamos la fruta ingresada por el usuario en el diccionario

if fruta in frutas:
    print("Las calorias son: ", frutas['Durasno' or 'Uva' or 'Manzana' or 'Sandia'], " calorias")
#SI el usuario no ingrese una fruta
else:
    print("Por favor verifique el nombre de la fruta")
