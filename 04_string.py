name = "Nicolas"
last_name = "Molina monroy"
print(name)
print(last_name)

full_name = name + last_name
print(full_name)

quote = "i'm nicolas"
print(quote)

quote2 = "She said 'hellow'"
print(quote2)

# format
template= "Hola, mi nombre es " + name + "y mi apellido es " +last_name
print("v1 ",template)

template = "hola, mi nombre {} y mi apellido es {}".format(name, last_name)

print("v2", template)

template = f"hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3", template)

nombre = "miguel"
apellido = "padilla"
edad = 24
template = f"hOLA, MI NOMBRE ES {nombre} {apellido} y mi edad es {edad}"

print("v4", template)