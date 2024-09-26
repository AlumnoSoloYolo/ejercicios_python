class Animal():
    def __init__(self,nombre = ""):
        self.nombre=nombre
        
    def decirNombre(self):
        return self.nombre
        
animal1 = Animal("perro")
print(animal1.nombre)


# Herencia

class Perro(Animal):
    
    def __init__(self):
        super().__init__("perro")

class Gato(Animal):
    
    def __init__(self):
        self.nombre="gato"
        



