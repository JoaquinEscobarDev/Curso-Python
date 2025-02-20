
nombre = 'Joaquin Andres'
last_name = 'Escobar Letelier'
caracter = "c"

#uso de sep=", " coloca todo lo que esta despues del = como separador
print("Hola", "Mundo", sep=", ")

#uso de end hace que aunque se tenga un salto de linea, se imprima al lado
print("Hola", end=" ")
print("Mundo")

#formate f-string permite colocar variables dentro de las llaves
frase = "hola mundo"
autor = "yo"
print(f"Frase:  {frase}, Autor: {autor}")

#formato con format las llaves se usan como marcador de posicion que se agregan en el orden dentro del .format
print("Frase: {}, Autor: {}".format(frase, autor))

#formato especifico dentro de las llaves {:.2f} se indica que debe tener 2 numeros despues del .
valor = 3.14167
print("Valor:  {:.2f}".format(valor))

#Salto de linea con \
#para evitar error de sintaxis al utilizar comillas en una cadena de texto se ocupa 'hola \'algo\''
#para colocar una ruta debes repetir los \ asi \\

#




#print("Hello world")
#print(1+1)
#print(nombre + ' (hola) ' + last_name)
# print(type(nombre))
# print(caracter)
#print(len(nombre))
#print(len(last_name))
# print(nombre.lower())
# print(nombre.upper())
# print(nombre.strip())

#print(nombre * 5)
# print(nombre[0])
# print(nombre[1])
# print(nombre[2])
# print(nombre[3])
# print(nombre[4])
# print(nombre[5])
# print(nombre[6])

