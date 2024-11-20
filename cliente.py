from zeep import Client

# URL del WSDL
wsdl_url = 'http://www.dneonline.com/calculator.asmx?WSDL'

# Crear el cliente SOAP
client = Client(wsdl=wsdl_url)

def add_numbers():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    result = client.service.Add(a, b)
    print(f"Resultado de la suma: {result}")

def subtract_numbers():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    result = client.service.Subtract(a, b)
    print(f"Resultado de la resta: {result}")

def multiply_numbers():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    result = client.service.Multiply(a, b)
    print(f"Resultado de la multiplicación: {result}")

def divide_numbers():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    if b == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        result = client.service.Divide(a, b)
        print(f"Resultado de la división: {result}")

def main():
    while True:
        print("\n=== Calculadora SOAP ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        choice = input("Seleccione una opción (1-5): ")
        
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            multiply_numbers()
        elif choice == "4":
            divide_numbers()
        elif choice == "5":
            print("Saliendo de la calculadora. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()




