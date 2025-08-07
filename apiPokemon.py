# https://pokeapi.co/api/v2/pokemon/

import requests

def obtener_datos_pokemon (nombre_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
    response =requests.get(url)
    
    if response.status_code ==200:
        
        pokemon_data = response.json()
        
        nombre = pokemon_data['name']
        print(f'Nombre_: {nombre.capitalize()}')
        
        tipos = [tipo['type']['name']for tipo in pokemon_data['types']]
        print (f"Tipos: { ','.join(tipos).capitalize()}")
        
        print ('\nEstadistica:')
        for stat in pokemon_data['stats']:
            nombre_stat = stat['stat']['name']
            valor_stat = stat ['base_stat']
            print(f"{nombre_stat.capitalize()}:{valor_stat}")
        
        habilidades = [habilidad['ability']['name'] for habilidad in pokemon_data['abilities']]
        print(f'\nHabilidades: {", ".join(habilidades).capitalize()}')
        
        print('\nMovimientos: ')
        movimientos = [movimiento['move']['name'] for movimiento in pokemon_data['moves'][:5]]
        print(f'  {", ".join(movimientos).capitalize()}')
        
        sprite = pokemon_data['sprites']['front_default']
        print(f'\nImagen del pokemon: {sprite}')
    else:
        print(f'Error: No se encontró el Pokemon {nombre_pokemon}')

nombre = input('Ingrese el nombre del pokemon a consultar: ')
obtener_datos_pokemon(nombre)
