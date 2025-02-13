x = 5 #variable global

def modify_global():
    global x 
    x+= 3
    print(f'valor modificado: {x}') 

modify_global()
print(x)