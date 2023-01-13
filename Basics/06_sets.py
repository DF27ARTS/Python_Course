
### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente <class 'dict'>

my_other_set = {"Tom", "Holland", 25}
print(type(my_other_set))  # ahora <class 'set'>

print(len(my_other_set))

my_other_set.add("Google")
print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("Google")  # Un set no admite repetidos
print(my_other_set)

print("google" in my_other_set)
print("Google" in my_other_set)

my_other_set.remove("Google")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Tom", "Holland", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"javascript", "python", "Typescript"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Java", "Kotlin"}))

print(my_new_set.difference(my_set))
