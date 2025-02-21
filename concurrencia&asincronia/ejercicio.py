#Implementar un sistema de descarga de archivos asincronica, 
#donde cada archivo tarde un tiempo variable en descargarse

import asyncio
import random

async def download(data):
    print("Descargando Archivos...")
    time = random.randint(1, 10)
    await asyncio.sleep(time)
    print(f'{data}: procesado.')
    
async def main():
    print('Inicio de descarga')
    result = ['python_1', 'python_2', 'python_3', 'python_4', 'python_5']
    await asyncio.gather(*(download(file) for file in result))
    print('Descarga completa')
    
asyncio.run(main())