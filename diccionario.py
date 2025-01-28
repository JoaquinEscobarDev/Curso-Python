numbers = {1:"uno", 2:"dos", 3:"tres"}
# print(numbers)

info = {
    "Nombre": "Joaquin",
    "Apellido": "Escobar",
    "Altura": 1.78,
    "Edad": 23
}
print(info)

del info["Edad"]
print(info)

claves = info.keys()

print(claves)

print(type(claves))

values = info.values()
print(values)

pairs = info.items()
print(pairs)

contacts = [
    {
        "Nombre": "Joaquin",
        "Apellido": "Escobar",
        "Altura": 1.78,
        "Edad": 23
    },
    {
        "Nombre": "Joaquin",
        "Apellido": "Escobar",
        "Altura": 1.78,
        "Edad": 23
    }
]

print(contacts)