#and
#Dos deben de dar true para que regrese true
print("and")
print("true and true =>", True and True)
print("true and False =>", True and False)
print("False and true =>", False and True)
print("False and False =>", False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input("Ingrese el numero de stock => ")
stock = int(stock)

print(stock >= 100 and stock <= 1000)

#Or
print("OR")
print("true or true =>", True or True)
print("true or False =>", True or False)
print("False or true =>", False or True)
print("False or False =>", False or False)

role = input("Digita el rol => ")
print(role == "admin" or role == "seller")