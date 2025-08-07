import requests
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO

nombre = input("Nombre del Pokémon: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    nombre = data["name"].capitalize()
    tipo = ", ".join([t["type"]["name"] for t in data["types"]])
    imagen_url = data["sprites"]["front_default"]
    
    # Crear ventana
    ventana = Tk()
    ventana.title(f"{nombre} - Pokémon")

    # Descargar imagen
    imagen_respuesta = requests.get(imagen_url)
    imagen = Image.open(BytesIO(imagen_respuesta.content))
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Mostrar imagen y datos
    Label(ventana, image=imagen_tk).pack()
    Label(ventana, text=f"Nombre: {nombre}").pack()
    Label(ventana, text=f"ID: {data['id']}").pack()
    Label(ventana, text=f"Altura: {data['height']}").pack()
    Label(ventana, text=f"Peso: {data['weight']}").pack()
    Label(ventana, text=f"Tipos: {tipo}").pack()

    ventana.mainloop()
else:
    print("Pokémon no encontrado.")
