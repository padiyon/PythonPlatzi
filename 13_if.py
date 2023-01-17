if True:
    print("Deberia ejecutarse")

if False:
    print("NUnca se ejecuta")

pet = input("Cual es tu mascota favorita? ")

if pet == "perro":
    print("Geneal tienes un perro")

elif pet == "gato":
    print("Tienes un gato")

elif pet == "pez":
    print("eres lo maximo")

else:
    print("No tienes ninguna mascota interesante")

numero = input("Ingresa un numero: ")
numero = int(numero)
calculo = numero % 2

if(calculo == 0):
    print("Numero par")
else:
    print("Numero inpar")



# stock = input("Digita el stock => ")
#
# if stock >= 100 and stock <= 1000:
#     print("el stock es correcto")
# else:
#     print("El stock es incorrecto")
