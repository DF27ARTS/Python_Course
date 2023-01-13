### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (25, 1.77, "Tom", "Holland", "instagram")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Tom"))
print(my_tuple.index("Tom"))
print(my_tuple.index("Holland"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(my_tuple)

my_tuple[4] = "Google"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
