
### File Handiling ###

import csv
import json
import os

""" .txt file """

# Leer, Excribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+")
txt_file.write(
    "Mi nombre es Tom \nMi apellido es Hollad \nTengo 25 años \nY mi lenguaje preferido es Python")

# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)


txt_file.write("\nAuque tambien me gusta Typescript")
print(txt_file.readline())

# txt_file.close()

# os.remove("Intermediate/my_file.txt")


""""""


""" .json files """

json_file = open("Intermediate/my_file.json", "w+")

json_text = {
    "name": "Tom",
    "lastname": "Holland",
    "age": 25,
    "languages": ["Python", "Typescript", "Javascript"],
    "website": "https//unsplash.in.com"
}

json.dump(json_text, json_file, indent=2)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])


""" .csv files """

# import csv

csv_file = open("Intermediate/my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "lastname", "age", "language", "website"])
csv_writer.writerow(
    ["Tom", "Holland", 25, "Python", "https//unsplash.in.com"])
csv_writer.writerow(["Angel", "", 40, "Python", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


""" .xlsx files """

# import xlsx # Deve instalarce el modulo

""" .xml files """

# import xml
