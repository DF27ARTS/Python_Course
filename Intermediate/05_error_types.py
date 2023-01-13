
### Error Types ###


# ModuleNotFoundError
# import maths # Descomentar para Error
import math


# SyntaxError
# print "¡Hola mundo!" # Descomentar para Error
print("¡Hola mundo!")


# NameError
language = "Spanish"  # Comentar para Error
print(language)


# IndexError
my_list = ["Python", "Javascript", "Typescript", "Kotlin", "Swift"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error


# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)


# KeyError
my_dict = {
    "Nombre": "Tom",
    "Apellido": "Holland",
    "Edad": 25,
    1: "Python"
}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])


# TypeError
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])


# ImportError
# from math import PI # Descomentar para Error
# from math import pi
# print(pi)


# ValueError
# my_int = int("10 años") # Descomentar para Error
my_int = int("10")
print(my_int)


# ZeroDivitionError
# print(4/0) # Descomentar para Error
print(4/2)
