
### Functions ###

def my_function():
    print("Esto es una funcion")


my_function()


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(sum_two_values("1", "7.6"))


def print_name(name, lastname, age):
    print(f"My name is {name} {lastname} y tengo {age} años")


print_name(lastname="Tom", name="Holland", age=25)
print_name("Tom", "Holland", 25)


def print_name_with_default(name="none", lastname="none"):
    print(f"My name is {name} {lastname}")


print_name_with_default("Tom", "Holland")
print_name_with_default()


def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "Google")
print_upper_texts("Hola")
