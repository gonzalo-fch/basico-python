#Problema 1 tutorial 1
#Debe devolver los elementos en las posiciones pares de una lista de entrada
#Recuerde que la posición inicial es 0 y cero es par
#Por ahora el programa entrega la lista completa (elementos en UNA línea separados por blanco)
#-----------------------------------------------------------------------------------
#Ejemplo de entrada
#a b c d e f g
#salida correspondiente
#['a', 'c', 'e', 'g']
lista = input().split()
lista2=[]

for x in range(0, len(lista), 2):
		lista2.append(lista[x])
		
lista=lista2
print(lista)
