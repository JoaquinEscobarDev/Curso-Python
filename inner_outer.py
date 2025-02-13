x = 'global' # variable global

#funcion externa
def outer_function():
    x = 'enclosing'

    #funcion interna
    def inner_function():
        x = 'local' #variable local
        print(x)
    
    inner_function()
    print(x)

outer_function()
print(x)