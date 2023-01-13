
### Classes ###

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, lastname, alias="Sin alias"):
        self.full_name = f"{name} {lastname} ({alias})"  # Propiedad publica
        self.__name = name  # Propiedad privada
        self.__lastname = lastname  # Propiedad privada

    def get_name(self):
        return self.__name

    def get_lastname(self):
        return self.__lastname

    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person("Tom", "Holland")
print(my_person.full_name)
my_person.walk()
print(my_person.get_name())
print(my_person.get_lastname())

my_other_person = Person("Angel", "Cruse", "Google")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Angle Cruse (Instagram)"
my_other_person.walk()
my_other_person.full_name = 725
my_other_person.walk()
