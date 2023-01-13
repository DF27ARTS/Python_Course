
### Loops ###

# while


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condicion es mayor o igual que 10")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se deteniene la ejecucíon")
        break
    print(f"Mi condicion es menor que 20 {my_condition}")

print("La ejecucion continúa")

# For

my_list = [35, 24, 64, 52, 30, 30, 17]

for element in my_list:
    print(element)


my_tuple = (25, 1.77, "Tom", "Holland", "instagram")
for element in my_tuple:
    print(element)

my_other_set = {"Tom", "Holland", 25}
for element in my_other_set:
    print(element)

my_dict = {
    "Nombre": "Tom",
    "Apellido": "Holland",
    "Edad": 25,
    "Languages": {
        "Python", "Javascript", "Typescript"
    },
    1: ["Azul", "verde", {"name": "Tom"}]
}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    elif element == 1:
        print("Element vale 1")
else:
    print("El bucle for para mi diccionario a terminado")
