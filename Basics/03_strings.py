
### Strings ###

my_string = "My string"
my_other_string = 'My other string'

print(len(my_string))
print(len(my_other_string))

print(my_string, " ", my_other_string)

my_new_line = "Este es un string\con salto de linea"
print(my_new_line)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)


# Formateo

name, lastname, age = "Tom", "Holland", 25

# print("Mi nombre es %s{name} %s{lastname} y tengo %d{age} años")
print("Mi nombre es {} {} y tengo {} años" .format(name, lastname, age))
print("Mi nombre es %s %s y tengo %d años" % (name, lastname, age))
print("Mi nombre es " + name + " " + lastname + " y tengo " + str(age) + " años")
print(f"Mi nombre es {name} {lastname} y tengo {age} años")  # My favorito

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# Divicíon

language_slice = language[1:3]  # slice javscript
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]  # print pto
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Fuccíones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
