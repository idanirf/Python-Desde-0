# LISTAS -> secuencia de elementos que pueden ser de cualquier tipo, incluso otras listas. Se declaran con corchetes.

# Declaración de una lista
lista = ["Ejemplo",1, "de", "una lista", 2.5, [1,2,3]]
print(lista)

# Acceso a los elementos de una lista
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[-3])
print(len(lista))

# Modificación de los elementos de una lista
lista[0] = "Ejemplo modificado"
print(lista)

# Tratamiento de listas
listaB = [1,2,3,4,5,6,7,8,9,10]
print(listaB[0:3])
print(listaB[3:6:2])
print(listaB[3:6])
print(listaB[3:])
print(listaB[:6])
print(listaB[::2])
print(listaB[::-1])

# Operaciones con listas
listaC = [1,2,3]
listaD = [4,5,6]
print(listaC + listaD)
print(listaC * 3)

# Métodos de las listas append
listaE = [1,2,3,4,5,6,7,8,9,10]
listaE.append(5)
print(listaE)

# Método insert
listaE.insert(6,7)
print(listaE)

# Método pop
listaE.pop()
print(listaE)

# Método remove
listaE.remove(7)
print(listaE)

# Método index
print(listaE.index(5))

# Método count
print(listaE.count(5))

# Método reverse
listaE.reverse()
