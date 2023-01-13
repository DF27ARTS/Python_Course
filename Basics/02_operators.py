
### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

print("hola" + "Python")
print("hola" + str(5))
print("hola " * 5)
print("hola " * (2 ** 3))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

print("break")

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" <= "Zola")    # Ordenacíon alfabética por ASCII
print(len("Hola") <= len("Zola"))    # Cuenta caracteres
print("aaaa" <= "aaaa")    # true
print("aaaa" <= "abaa")    # false
print("Hola" >= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores logicos ###

print(3 > 4 and "Hola" > "Python")  # &&
print(3 > 4 or "Hola" > "Python")  # ||
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or "Hola" < "Python" and 4 == 4)
print(not (3 > 4))  # !true
