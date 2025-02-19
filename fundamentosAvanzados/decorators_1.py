def mi_decorator(function):
    def nueva_funcion(parametro):
        #Codigo que se ejecuta antes de llamar a la funcion original 
        print("Antes de ejecutar la funcion")
        
        #llama a la funcion original con el parametro recibido
        function(parametro)
        
        #codigo que se ejecuta despues de llmar a l funcion original
        print("Despues de ejecutar la funcion")
        
    return nueva_funcion

@mi_decorator #Aplicamos el decorador usando @
def mi_funcion(parametro):
    #funcion original que sera decorada
    print(f"Ejecutando la funcion con el parametro: {parametro}")
    
#ejemplo de uso
mi_funcion("ejemplo")