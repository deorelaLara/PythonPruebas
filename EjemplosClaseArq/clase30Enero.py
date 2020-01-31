
print("CICLO FOR")
#var = range(0, 10)

#Iteramos la variable var
#for i in var:
 #   print(i)
#Imprime solamente los numeros pares en el rango
var1 = range(0, 11)
for i in var1:
    if i % 2:
        print(i)

"""var2 = range(0, 11, 2)
for i in var2:
    print(i)"""


#LISTAS
print("LISTAS")
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []

for i in range(0, len(list)):
    if i % 2 == 0:
        list2.append(i)

#print(list2)

#LISTA COMPRIMIDA
lista = [i for i in range(0, 10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""Crea un salto de 2 en 2 --- el primer numero define donde inicia la lista,
 el segundo el limite y el tercero podemos asignarle un salto"""
list3=[i for i in range(0, 10, 2)]

"""
remplaza las vocales por un - / en la lista 5 el codigo esta mejorado
"""
lista4 = [i if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' else '-' for i in 'hola mundo']
lista5 = [i if i in 'aeiou' else '-' for i in 'hola mundo']
#print(lista4)
#print(lista5)

#GENERAR LISTA CON LAS PRIMERAS 1000 POTENCIAS DE 2
potencia = [2**i for i in range(0, 100)]
#print(potencia)

#LISTA DE LISTAS
listaPrincipal = [list, list2, list3, lista4, lista5]


print("     DICCIONARIOS")
ord('a')
chr(97)
ord(chr(97) +1)
chr(ord('a') +1)

