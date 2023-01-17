# Crud create, read , update & delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700) #Añade nuevo elemento a la lista
print(numbers)

numbers.insert(0, "hola") #Inserta valores a la lista, el primer elemento es la coordenada
print(numbers)

numbers.insert(3, "change")
print(numbers)

tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks # Combino dos listas e hizo una nueva
print(new_list)

index = new_list.index('todo 2') #Te dice en que posicion esta "todo 2"
print(new_list.index('todo 2'))
new_list[index] = "todo change"
print(new_list)

new_list.remove('todo 1') #Elimino todo 1 de la lista
print(new_list)

new_list.pop() #Elimina el ultivo valor
print(new_list)

new_list.pop(0) #Tambien se puede con la posicion
print(new_list)

new_list.reverse() #Voltea la lista
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort() #Ordena del mayor a menor
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort() #Ordena orden alfabetico primer letra, no puede ordenar datos mezclados
print(strings)
