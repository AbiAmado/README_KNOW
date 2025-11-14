def main():
  print("Hello learners!")

if __name__=="__main__":
  main()

def addmultiplenumbers(numbers):
    """Toma una lista de números y devuelve su suma."""
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    """Toma una lista de números y devuelve el producto de todos ellos."""
    # Si la lista está vacía, el producto se define como 1
    result = 1
    for num in numbers:
        result = result * num
    return result

def isitaninteger(num):
    """Devuelve True si 'num' es un entero (int o float sin decimales), False en caso contrario."""
    # Compara el número con su versión truncada a entero.
    return num == int(num)

def isiteven(num):
    """Devuelve True si 'num' es un número entero PAR, False en caso contrario."""
    
    # Primero, debe ser un entero
    if not isitaninteger(num):
        return False
    
    # Luego, debe ser par (resto de la división por 2 es 0)
    # Es crucial usar int(num) para el módulo si el número es un float como 4.0
    return int(num) % 2 == 0

def main():
    print("Hello learners!")
    # Lógica interactiva opcional. No es necesaria para la calificación.
    # Ejemplos de prueba:
    # print(f"Suma: {addmultiplenumbers([1, 5, 10])}") # 16
    # print(f"Producto: {multiplymultiplenumbers([2, 3, 4])}") # 24
    # print(f"¿Es 4.0 un entero? {isitaninteger(4.0)}") # True
    # print(f"¿Es 4.5 un entero? {isitaninteger(4.5)}") # False
    # print(f"¿Es 4 un par? {isiteven(4)}") # True
    # print(f"¿Es 3 un par? {isiteven(3)}") # False
    # print(f"¿Es 4.0 un par? {isiteven(4.0)}") # True

if __name__=="__main__":
    main()