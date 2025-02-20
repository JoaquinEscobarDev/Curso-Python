import json

# #lee el archivo
# with open('products.json', mode='r') as file:
#     products = json.load(file)


# #Muestra el contenido
# for product in products:
#     print(f"Product: {product['name']}, Price: {product['price']}")

#Nuevos datos Json
file_path = 'products.json'

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargerMaster",
    "category": "Accesories",
    "entry_date": "2024-07-01"
}

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)