my_dict = {}
print(type(my_dict))

my_dict = {
    'avion' : 'bla bla bla',
    'name' : 'nicolas',
    'last name' : 'molina',
    'age' : 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last name'])
print(my_dict.get('age')) #Para obtener valores que tal vez no existen

print('avion' in my_dict) #Para ver si existe dentro del diccionario
print('otroque' in my_dict)