text = "Ella sabe programar en Python"

'''
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print("Elegiste bien!")
else:
    print("Tambien elegiste bien")
'''
size = len("amor    ") #Longitud
print(size)

print(text)
print(text.upper()) #Todo a mayusculas
print(text.lower()) #Todo a minuscula
print(text.count("a")) #Cuenta cuantas a

print(text.swapcase()) #Invierte las mayusculas y las minusculas
print(text.startswith("Ella")) #Evalua si empieza con ella
print(text.endswith("Rust")) #Evalua si el texto termina con rust
print(text.replace("Python", "Go")) #Reemplaza python con go

text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize()) #Pone el primer caracter en mayuscula
print(text_2.title()) #Pone en mayusculas cada primer letra en las frases
print(text_2.isdigit()) #Evalua si es un digito el texto
print("123".isdigit()) #Ahora con digitos