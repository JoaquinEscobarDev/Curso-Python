def add(a: int, b: int):
    return a + b

def sust(a: int, b: int):
    return a - b

def mult(a: int, b: int):
    return a * b

def div(a: int, b: int) -> float:
    if b == 0:
        raise ValueError('No se puede dividir por 0')
    
    return a / b

if __name__ == "__main__":
    print("Operaciones")
    res1 = add(3,4)
    res2 = sust(5,9)
    res3 = mult(5,9)
    res4 = div(5,100)
    print(f'Suma: {res1}')
    print(f'Resta: {res2}')    
    print(f'Multiplicacion: {res3}')
    print(f'Division: {res4}')