# 1 Hacer un pequeño tutorial en un Google Dosc de cada una de las funciones de 
# debug con VsCode.
# 2 Hacer el ejemplo con una un programa que tenga 4 funciones : sumar, restar, 
# multiplicar y dividir.
# 3 Explicar el panel dónde se ven las variable locales y globales.
x = 10
y = 5

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"
    
print("La suma de {} y {} es {}".format(x,y,sumar(x,y)))
print("La resta de {} y {} es {}".format(x,y,restar(x,y)))
print("La multiplicación de {} y {} es {}".format(x,y,multiplicar(x,y)))
print("La división de {} y {} es {}".format(x,y,dividir(x,y)))



        

