#BOLETÍN EJERCICIOS PYTHON

#1 Imprime "Hola, mundo!" en la pantalla. 
print("Hola, mundo!")

#2 Calcula la suma de dos números ingresados por el usuario. 

num1 = int(input("Dame un numero entero: "))

num2 = int(input("dame otro numero entero: "))

suma = num1 + num2

print("La suma de {} y {} es: {}".format(num1,num2,suma))

#3 Calcula el área de un triángulo con la fórmula: Área = (base * altura) / 2. 
base = float(input("dame la base de un triangulo: "))
altura = float(input("dame la altura de un triangulo: "))

areaTriangulo = base * altura /2

print("El area de un triangulo con "+str(base)+" y "+str(altura)+" es: "+ str(areaTriangulo))

#4 Convierte grados Celsius a Fahrenheit: F = °C × (9/5) + 32.

tempCelsius = int(input("Dime una temperatura en grados celsius"))

tempFarenheit = tempCelsius * (9/5) + 32

print(str(tempCelsius)+"ºC equivale a "+ str(tempFarenheit)+"ºF")

 
#5 Calcula el factorial de un número.
num = 10
factorial = 1
for i in range(1,11):
    factorial*=i

print("El factorial de {} es: {}".format(num,factorial))

#6 Verifica si un número es par o impar. 
num = 20
if num % 2 == 0:
    print("{} es un numero par".format(num))
else:
    print("{} es un numero impar".format(num))

#7 Calcula el máximo común divisor (MCD) de dos números. 
num1 = 10
num2 = 20
divNum1 = []
divNum2 = []

for i in range(1, num1+1):
    if num1 % int(i) == 0:
        divNum1.append(i)
        
print("divisores de {} son: {}".format(num1, divNum1))

for i in range(1, num2+1):
    if num2 % int(i) == 0:
        divNum2.append(i)
        
print("divisores de {} son: {}".format(num2, divNum2))

mcd = 0
for i in range(0, len(divNum1)):
    for j in range(0, len(divNum2)):
        if divNum1[i] == divNum2[j]:
            mcd = divNum1[i]
           
            
print("el máximo común divisor de {} y {} es: {}".format(num1,num2,mcd))
    


#8 Imprime los números del 1 al 10 usando un bucle for. 
for i in range(1,11):
    print(i)

#9 Calcula la suma de los números del 1 al 100. 
suma = 0
for i in range(1,101):
    suma+=int(i)
print("la suma de los 100 primeros numeros es: "+ str(suma))   

#10 Crea una lista de números y calcula su promedio. 
listaNum= [1,3,5,7,9,11,13,15]
sumaLista= 0
contador= 0

for x in listaNum:
    sumaLista+= x
    contador+=1

promedio = sumaLista/contador

print("la media es: "+ str(promedio))
    

#11 Crea una clase llamada Persona con atributos nombre y edad. Luego, crea un objeto de tipo Persona e imprime sus atributos.

#12 Crea una clase llamada Rectangulo con atributos ancho y altura. Agrega un método para calcular el área del rectángulo y otro para calcular su perímetro. 

#13 Crea una clase llamada Estudiante con atributos nombre, edad y curso. Crea varios objetos de tipo Estudiante y almacénalos en una lista. Luego, itera sobre la lista e imprime la información de cada estudiante.  

#14 Crea una clase llamada CuentaBancaria con atributos titular y saldo. Agrega métodos para depositar y retirar dinero de la cuenta.  

#15 Crea una clase llamada Coche con atributos marca y modelo. Crea un método que imprima la información del coche en un formato legible. 

#16 Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico. Luego, crea dos clases derivadas, Perro y Gato, que hereden de Animal y sobrescriban el método hablar para imprimir mensajes diferentes. 

#17 Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área de la figura. Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica y sobrescriban el método area para calcular el área específica de cada figura.

#18 Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método informacion que imprima la información del vehículo. Luego, crea clases derivadas como Coche y Bicicleta que hereden de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.

#19 Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. Luego, crea clases derivadas como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban el método tocar para imprimir mensajes diferentes.

#20 Crea una clase base llamada Empleado con atributos nombre y salario, y un método calcular_salario_anual que calcule el salario anual del empleado. Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y añadan atributos y métodos específicos de cada tipo de empleado.
