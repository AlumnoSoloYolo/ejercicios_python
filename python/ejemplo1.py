# print ("hola clase DAW")


# if-elif-else
edad = 29
if edad >= 28:
    print("No tienes derecho a beca")
elif edad >= 18 and edad < 28:
    print("Tienes derecho a beca")
else:
    print("Eres menor de edad")


# for
for i in range(6, 22):
    print(i)
print("fin")


# for anidado
for i in range(0, 21):
    for j in range(0, 21):
        print("posicion ["+ str(i) +","+str(j)+"]")
        
# for de lista 
lista = ["Lolo","Sara","Carlos","Leo"]
for x in lista:
    print("Elemento de la lista "+ x)
    

