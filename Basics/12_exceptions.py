
### Exceptions Handling ###

numberOne = 5
numberTwo = 1
numberOne = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except:
    # se ejecuta si se produce una excepcion
    print("Se a producido un error")


# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except:
    print("Se a producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecucion continua")


# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except ValueError:
    print("Se a producido un ValueError")
except TypeError:
    print("Se a producido un TypeError")


# Captura de la onformacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except ValueError as ValueError:
    print(f"Se a producido un ValueError: {ValueError} ")
except Exception as error:
    print(f"Se a producido un ValueError: {error} ")
