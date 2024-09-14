# Escribe un programa que pida al usuario su nombre y apellido, y luego los imprima juntos en un mensaje de saludo.

nombre = input("Por favor, ingresa tu nombre: ")

apellido = input("Por favor, ingresa tu apellido: ")

print(nombre + " " + apellido)


# Crea una variable llamada precio con el valor 100. Calcula el precio con un descuento del 15% y muestra el precio final.

precio = 100
descuento = 0.15
precio_final = precio - (precio * descuento)
print("Precio con descuento: ", precio_final)


# Escribe un programa que pida al usuario su edad y luego determine si es mayor o menor de edad.

edad = int(input("Edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


# Crea un programa que pida al usuario un número y determine si es par o impar.

numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


# Escribe un programa que pida al usuario dos números y luego calcule su suma, resta, multiplicación y división.

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "Indefinida (no se puede dividir por 0)"

print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")


# Crea un programa que pida al usuario su calificación y luego imprima el mensaje "Aprobado" si la calificación es mayor o igual a 70, o "Reprobado" si la calificación es menor que 70.

calificacion = float(input("Calificacion: "))
if calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")


# Escribe un programa que pida al usuario dos números y luego determine cuál es el mayor.

numero1 = float(input("Primer numero: "))
numero2 = float(input("Segundo numero: "))

if numero1 > numero2:
    print("El primer número es mayor.")
elif numero1 < numero2:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")


# Crea un programa que pida al usuario su nombre y luego imprima un mensaje de bienvenida con su nombre.

nombre = input("Ingrese su nombre: ")
print(f"Bienvenido, {nombre}")


# Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar de ese número hasta el 10.

numero = int(input("Ingrese un numero: "))
print(f"Tabla de multiplicar {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Crea un programa que pida al usuario dos números y luego calcule su promedio.

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

promedio = (numero1 + numero2) / 2
print(f"El promedio de los dos números es: {promedio}")


