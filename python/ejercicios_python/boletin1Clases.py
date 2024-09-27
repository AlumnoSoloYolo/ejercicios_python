from abc import ABC, abstractmethod

#11 Crea una clase llamada Persona con atributos nombre y edad. Luego, 
# crea un objeto de tipo Persona e imprime sus atributos.

class Persona():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
persona1 = Persona("Pepa", 29)

print("nombre: {}\n edad: {}".format(persona1.nombre, persona1.edad))


#12 Crea una clase llamada Rectangulo con atributos ancho y altura. 
# Agrega un método para calcular el área del rectángulo y otro para calcular su perímetro. 

class Rectangulo():
    def __init__(self, ancho, altura):
        self.ancho=ancho
        self.altura=altura
        self.area=self.calcular_area()
        self.perimetro=self.calcular_perimetro()
        
    def calcular_area(self):
            return self.ancho * self.altura
        
    def calcular_perimetro(self):
            return 2 * (self.ancho + self.altura)
        
rectangulo1 = Rectangulo(10, 15)

print(f"ancho: {rectangulo1.ancho}")
print(f"altura: {rectangulo1.altura}")
print(f"área: {rectangulo1.area}")
print(f"perímetro: {rectangulo1.perimetro}")
#print(f"area: {rectangulo1.calcular_area()}")
#print(rectangulo1.calcular_area())


#13 Crea una clase llamada Estudiante con atributos nombre, edad y curso. 
# Crea varios objetos de tipo Estudiante y almacénalos en una lista. Luego, 
# itera sobre la lista e imprime la información de cada estudiante. 
class Estudiante():
    def __init__(self, nombre, edad, curso):
        self.nombre=nombre
        self.edad=edad
        self.curso=curso
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}"

estudiante1 = Estudiante("Jose", 26, "1º DAM")
estudiante2 = Estudiante("Álvaro", 26, "1º DAW")
estudiante3 = Estudiante("Luna", 27, "2º DAM")

listaEstudiantes = []

listaEstudiantes.append(estudiante1)
listaEstudiantes.append(estudiante2)
listaEstudiantes.append(estudiante3)

for i in range(0, len(listaEstudiantes)):
    print(listaEstudiantes[i])


#14 Crea una clase llamada CuentaBancaria con atributos titular y saldo. 
# Agrega métodos para depositar y retirar dinero de la cuenta.  

class CuentaBancaria():
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
        
    def depositar(self, dinero):
        self.saldo = self.saldo + dinero
    
    def retirar(self, dinero):
        self.saldo = self.saldo - dinero

cuentaBancaria1 = CuentaBancaria("Lolito", 3000)

cuentaBancaria1.depositar(200)
print(cuentaBancaria1.saldo)

cuentaBancaria1.retirar(100)
print(cuentaBancaria1.saldo)

#15 Crea una clase llamada Coche con atributos marca y modelo. 
# Crea un método que imprima la información del coche en un formato legible. 

class Cochesito():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
    
    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}"
 
miCoche = Cochesito("Peugeot", "308")   
print(miCoche.__str__())

#16 Crea una clase base llamada Animal con un método hablar que imprima 
# un mensaje genérico. Luego, crea dos clases derivadas, Perro y Gato, que hereden 
# de Animal y sobrescriban el método hablar para imprimir mensajes diferentes. 
class Animal():  
    def hablar():
        return "Hago ruidos por la boca"

class Perro(Animal):
    def hablar():
        return "guau guau"
    
class Gato(Animal):
    def hablar():
        return "miau miua"

animal1 = Animal()
perro1 = Perro()
gato1 = Gato()


print(animal1.hablar())
print(perro1.hablar())
print(gato1.hablar())
   

#17 Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, 
# y un método area que calcule el área de la figura. Luego, crea clases derivadas 
# como Rectangulo y Triangulo que hereden de FiguraGeometrica y sobrescriban el método 
# area para calcular el área específica de cada figura.
class FiguraGeometrica(ABC):
    def __init__(self, anchura, altura):
        self.anchura=anchura
        self.altura=altura
        
    @abstractmethod
    def calcArea(self):
        pass
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, anchura, altura):
        super().__init__(anchura, altura)
    
    def calcArea(self):
        area=self.anchura*self.altura
        return area
    
class Triangulo(FiguraGeometrica):
    def __init__(self, anchura, altura):
        super().__init__(anchura, altura)
    
    def calcArea(self):
        area=self.anchura*self.altura/2
        return area

#18 Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método 
# informacion que imprima la información del vehículo. Luego, crea clases derivadas 
# como Coche y Bicicleta que hereden de Vehiculo y añadan atributos y métodos específicos 
# de cada tipo de vehículo.
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        
        
    def informacion(self):
        return f"marca: {self.marca}\nmodelo: {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, combustible):
        super().__init__(marca, modelo)
        self.combustible=combustible
    
    def tocar_claxon():
        print("Tocando el claxon")
        
class Bicicleta():
    def __init__(self, marca, modelo, color ):
        super().__init__(marca, modelo)
        self.color=color
    
    def pedalear():
        print("Pedaleando")
        
coche1 = Coche("peugeot", "308", "diesel")
print(coche1.informacion())



#19 Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un 
# mensaje genérico. Luego, crea clases derivadas como Piano y Guitarra que hereden de 
# InstrumentoMusical y sobrescriban el método tocar para imprimir mensajes diferentes.
class InstrumentoMusica():
    def __init__(self, tipo):
        self.tipo=tipo
    
    def tocarInstrumento(self):
        return "DO LA# MI SOL"

class Piano(InstrumentoMusica):
    def __init__(self, tipo, marca):
        super().__init__(tipo)
        self.marca=marca
        
    def tocarInstrumento(self):
        return "DO LA# MI SOL"

instrumentoMusica1 = InstrumentoMusica("cuerda")

print(instrumentoMusica1.tocarInstrumento())

piano1 = Piano("cuerda", "yamaha")

print(piano1.tocarInstrumento())


#20 Crea una clase base llamada Empleado con atributos nombre y salario, y un método 
# calcular_salario_anual que calcule el salario anual del empleado. Luego, crea clases 
# derivadas como Gerente y Programador que hereden de Empleado y añadan atributos y métodos 
# específicos de cada tipo de empleado.

class Empleado():
    def __init__(self, nombre, salario):
        self.nombre=nombre
        self.salario=salario
    
    def calcular_salario_anual(self):
        return self.salario * 12

empleado1 = Empleado("Sara", 2000)
empleado1.calcular_salario_anual()

print(empleado1.calcular_salario_anual())


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    def __str__(self):
        return f"nombre: {self.nombre}\nsalario: {self.salario}\ndepartamento: {self.departamento}"

class Programador(Empleado):
    def __init__(self, nombre, salario, puesto):
        super().__init__(nombre, salario)
        self.puesto=puesto


gerente1 = Gerente("Manuel", 2200, "tecnológico")
programador1 = Programador("Ana", 1500, "frontend")

print(gerente1.__str__())

