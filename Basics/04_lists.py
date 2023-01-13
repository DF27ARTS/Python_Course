
### Lists ###

# my_list = [2, 3, 4, 5, True, "Hello"]  # array javascript
# print(my_list)

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 64, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Tom", "Holland"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(23, my_other_list[-1])
print(24, my_other_list[len(my_other_list) - 1])
print(my_other_list[-3])
print(my_other_list.count("Tom"))
print(my_list.count(30))

age, height, name, lastname = my_other_list
print(name)

name, height, age, lastname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
print(height)
print(age)
print(lastname)

# [35, 1.77, 'Tom', 'Holland', 35, 24, 64, 52, 30, 30, 17]
lists = my_other_list + my_list
print(lists)

print([1, 2, 3, 4])


my_other_list.append("Google")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_pop_element = my_list.pop()  # Saca el ultimo elemento
print(my_pop_element)
print(my_list)

my_pop_element = my_list.pop(2)  # Saca el elemento que le inidicaste
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()


my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list[0])
