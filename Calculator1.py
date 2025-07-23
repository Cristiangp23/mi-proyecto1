def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: No se puede dividir por cero"
    return x / y

print("Seleccione operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

