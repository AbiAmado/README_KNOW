# 1. Obtener la primera entrada del usuario
# La función input() siempre devuelve texto (string).
numero1_texto = input("Escribe el primer numero: ")

# 2. Obtener la segunda entrada del usuario
numero2_texto = input("Escribe el segundo numero: ")

# 3. Convertir el texto a números enteros (int) y sumarlos
# Usamos int() para convertir el texto en números para que Python pueda hacer la suma matemática.
resultado = int(numero1_texto) + int(numero2_texto)

# 4. Imprimir el resultado
# Usamos una "f-string" (la 'f' antes de las comillas) para incluir el resultado fácilmente en el texto.
print(f"\nEl resultado de la suma es: {resultado}")