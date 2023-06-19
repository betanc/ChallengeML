import json
#import pip._vendor.requests 

#url = "https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"

#response = requests.get(url)
#data = response.json()

#with open("datos.json", "w") as file:
#     json.dump(data, file)


import aiohttp
import aiofiles
import asyncio


async def ObtenerdatosURL(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

async def almacenar(data, filename):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(json.dumps(data))

async def main():
    url = 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
    json_filename = 'datos.json'

    # Obtener los datos 
    data = ObtenerdatosURL(url)

    # Guardar 
    await almacenar(data, json_filename)

# Ejecutar 
asyncio.run(main())

