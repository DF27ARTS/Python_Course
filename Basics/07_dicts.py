
### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Tom",
    "Apellido": "Holland",
    "Edad": 25,
    1: "Python"
}

my_dict = {
    "Nombre": "Tom",
    "Apellido": "Holland",
    "Edad": 25,
    "Languages": {
        "Python", "Javascript", "Typescript"
    },
    1: ["Azul", "verde"]
}

print(my_dict)
print(my_other_dict)

my_dict["Nombre"] = "Cruse"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Ciudad"] = "Paris"
print(my_dict)

del my_dict["Ciudad"]
print(my_dict)

print("Tom" in my_dict)
print("Holland" in my_dict)

print("breack")

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Calle"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "calle"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Google")
print(my_new_dict)

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
