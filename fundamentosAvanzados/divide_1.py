def divide(a:int, b: int) -> float:
    if not isinstance(a,int) or not isinstance(b, int):
        raise TypeError('Ambos parametros deben ser enteros')
        
        # print('Error: Ambos parametros deben ser enteros o flotantes')
        # return None
    #Verificamos que el divisor no sea 0
    if b==0:
        raise TypeError('El divisor no puede ser 0')
        
        # print('El divisor no puede ser 0')
        # return None

    return a/b

try: 
    res = divide(10,'2') #Error de tipo
    print(res)
except TypeError as e:
    print(f'Error: {e}')
    


res1 = divide(10,2)
res2 = divide(10,0)
res3 = divide(10,'2')