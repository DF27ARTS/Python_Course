
### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
numeros de 1 a 100 (ambos incluidos y con un salto de linea entre
cada impresion), sustitullendo lo siguiente:
 - Multiplos de 3 por la palabra "fizz"
 - Multiplos de 5 por la palabra "buzz"
 - Multiplos de 3 y 5 a la vez por la palabra "fizzbuzz"
"""


def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()


"""
¿ES UN ANAGRAMA?
Escribe una funcion que reciba dos palabras (String) y retorne
verdadero o falso (Bool) segun sean o no anagramas.
- Un anagrama conciste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan,
- Dos palabras exactamente iguales no son anagramas.
"""


def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("amor", "rome"))


"""
LA SUCESIIÓN DE FIBONACCI
Escribe un programa que imprima los primeros 50 numeros de la sucesion
de Fibonacci empezando en 0 
- La serie de Fibonacci se compone por una sucesion de numeros en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci():
    prev = 0
    next = 1

    for _ in range(0, 50):
        print(_)
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()


"""
¿ES UN NUMERO PRIMO?
Escribe un programa que se encargue de comproba si un numero es primo o no.
Hecho esto, imprime los numeros primos entre 1 y 100.
"""


def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)


is_prime()


"""
INVIRTIENDO CADENAS
Crea un programa que invierta una cadena de texto 
sin usar funciones propias del lenguaje que lo agan de forma automatica
- Di le pasamos "Hola mundo" nos retornaria "odnum aloH"
"""


def reverse(text):
    text_len = len(text)
    reverse_text = ""

    for index in range(0, text_len):
        reverse_text += text[text_len - index - 1]

    return reverse_text


print(reverse("Hola Mundo"))
