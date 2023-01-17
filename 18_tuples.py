numbers = (1, 2, 3, 5)
strings = ("nico", "zule", "santi")
print(numbers)
print("o =>", numbers[0])
print("-1 =>", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#Crud
#numbers.append(10)
print(numbers)
#numbers[1] = "change"
#Las tuplas no se pueden modificar
print(strings)
print(strings.index("zule"))
print(strings.count("nico"))

my_list = list(strings) #Convierte a lista
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list) #Convierte a tupla
print(my_tuple)