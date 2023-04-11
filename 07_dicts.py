# Dictionaries ✔

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "id": 1,
    "name": "edgard",
    "lastname": "pazos",
    "languages": ["JavaScript", "Python"]
}

print(my_other_dict)
print(my_other_dict["id"])
print(my_other_dict["name"])
print(my_other_dict["languages"][0])