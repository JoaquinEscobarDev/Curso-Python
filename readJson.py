import json

#lee el archivo
with open('products.json', mode='r') as file:
    products = json.load(file)


#Muestra el contenido
for product in products:
    print(f"Product: {product['name']}, Price: {product['price']}")

