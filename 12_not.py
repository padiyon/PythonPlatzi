print(not True)
print(not False)

#and
print("not and")
print("not True and true = >", not (True and True))
print("not True and False =>", not (True and False))
print("False True and true =>", not (False and True))
print("False True and False =>", not (False and False))

stock = input("Ingrese el numero de stock => ")
stock = int(stock)

print(not(stock >= 100 and stock <= 1000))
