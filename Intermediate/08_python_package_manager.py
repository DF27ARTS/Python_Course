
### Python Package Manager ###

# PIP https://pypi.org

# pip install pip
# pip --version

from mypackage import arithmetics
import requests  # pip install requests
import pandas  # pip install pandas
import numpy  # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 64, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)


# pip list
# pip uninstall pandas
# pip show numpy

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
# print(response.json())


# Arithmetic Package


print(arithmetics.sum_two_values(2, 4))
