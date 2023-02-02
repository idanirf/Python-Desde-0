# ¿Qué son las cadenas? -> colecciones inmutables de caracteres. Se declaran con comillas simples o dobles

# Declaración de una cadena
cadena = "Hola Mundo"
cadena2 = 'Hola Mundo'
cadena3 = "Hola Mundo\ncomo estas?"
cadena4 = """Esto es una cadena con muchasss lineas"""

# Imprimir una cadena
print(cadena)
print(cadena2)
print(cadena3)
print(cadena4)

# Operaciones con cadenas
concatenacion = cadena + " " + cadena2 + 'hasta aquí'
print(concatenacion)
multiplicacion = 'Hola'*3
print(multiplicacion)

# Metodo count
ejemplo = "Hola Mundo, Hola Mundo, Hola Mundo"
print(ejemplo.count("o",0,10))
print(ejemplo.count("o"))

# Metodo find
ejemploFind = "Esto es un ejemplo"
print(ejemploFind.find("es"))
print(ejemploFind.find("es",0,10))

# Metodo replace
ejemploReplace = "Esto es un ejemplo"
print(ejemploReplace)
ejemploReplace.replace("ejemplo", "Ejemplo",1)
print(ejemploReplace)

# Metodo split
ejemploSplit = "Esto es un ejemplo"
print(ejemploSplit.split(" "),1)
print(ejemploSplit.split(" "))

# Metodo join
ejemploJoin = "Esto es un ejemplo"
separador = "-"
secuencia = ["Esto", "es", "un", "ejemplo"]
print(separador.join(secuencia))
