AÑO_ACTUAL = 2024
def calcular_edad(año_nacimiento):
    return año_nacimiento - AÑO_ACTUAL

def main():
    nombre = input("Ingresa tu nombre: ")
    año_nacimiento = int(input("Ingresa tu año de nacimiento: "))
    edad = calcular_edad(año_nacimiento)
    print(f"Hola {nombre}, tienes {edad} años.")
    print(f"Nacio el año {año_nacimiento}.")

main()