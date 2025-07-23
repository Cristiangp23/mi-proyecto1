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

while True:
    opcion = input("Ingrese opción (1/2/3/4): ")

    if opcion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números.")
            continue

        if opcion == '1':
            print(num1, "+", num2, "=", suma(num1, num2))
        elif opcion == '2':
            print(num1, "-", num2, "=", resta(num1, num2))
        elif opcion == '3':
            print(num1, "*", num2, "=", multiplicacion(num1, num2))
        elif opcion == '4':
            print(num1, "/", num2, "=", division(num1, num2))

        siguiente_calculo = input("¿Desea realizar otra operación? (si/no): ")
        if siguiente_calculo == "no":
            break
    else:
        print("Opción inválida")