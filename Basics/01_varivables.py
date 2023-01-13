
# Variables

my_variable_string = "My string varible"
print(my_variable_string)

my_variable_number = 7
print(my_variable_number)

my_int_to_string = str(my_variable_number)
print(my_int_to_string)
print(type(my_int_to_string))

my_variable_boolean = True
print(my_variable_boolean)


# Concatenacion de variables rn un print
print(my_variable_string, my_variable_number, my_variable_boolean)

# Funciones del sistema
print(len(my_variable_string))

# Variables en una sola linea
name, lastname, age = "tom", "holland", 25
print("Me llamo:", name, lastname, "y tengo", age, "años")


# Inputs
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Forzamos el tipo
address: str = "Mi string"
address = 5

print(type(address))
