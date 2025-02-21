import threading
import time


# Funcion que simula el proceso de una solicitud


def process_request(request_id):
    print(f"Procesando solicitud {request_id}")
    time.sleep(3)
    print(f"Solicitud {request_id} completada")


threads = []

for i in range(3):
    # Crear nuevo hilo que ejecutara la funcion
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()
    
#Esperar que todos los hilos terminen 
for thread in threads:
    #Asegura que todos los hilos terminen
    thread.join()
    

print('Todas las solicitudes completadas')
