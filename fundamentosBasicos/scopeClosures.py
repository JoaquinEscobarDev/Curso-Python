x = 100

def local_function():
    x = 10  # variable local
    print(f"el valor de la variable es: {x}")

def show_global():
    print(f'El valor de la variable global es: {x}')



local_function()
print(x)
