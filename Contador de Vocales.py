#Realizar un programa que permita ingresar una frase y muestre cuantas vocales tiene la frase 
#ingresada. Ejemplo. De la frase “Universidad estatal de milagro” el resultado mostrado seria: 
#La frase cuenta con 12 vocales.

fra = input('Ingrese una frase: ')
conta = 0 
for i in fra:
    if i in 'aeiou':
        conta = conta + 1
print('La cantidad de vocales en esta frase son:', conta)