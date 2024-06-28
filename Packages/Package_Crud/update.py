from Packages.Package_Input.Input import get_string, get_int, get_confirm

from datetime import datetime

def update_title() -> str:
    title = get_string("Ingrese el nuevo título de la película: ",max_length=30,min_length=1)
    title = title.title()
    print("Título cambiado con éxito.")
    return title

def update_genre(genres: list) -> str:
    genre = get_string("Genero: ", max_length=18,min_length=1)
    genre = genre.capitalize()
    while genre not in genres:
        print("Escriba un género válido \b")
        print(",".join(genres))
        genre = get_string("Genero: ", max_length=18,min_length=1)
        genre = genre.capitalize()
    print("Género cambiado con éxito.")
    return genre

def update_year() -> int:
    actual_year = datetime.now().year
    year = get_int("Año de lanzamiento: ",error_message=f"El año debe estar entre 1888 y {actual_year}\n",min=1888,max= actual_year)
    print("Año de lanzamiento cambiado con éxito.")
    return year

def update_length() -> int:
    length = get_int("Duración: ",min=0,max=999999999999999999999999)
    print("Duración cambiada con éxito.")
    return length

def update_atp() -> bool:
    atp = get_confirm("¿Es apta para todo público? [S/n]\n ")
    print("Apta para todo público cambiada con éxito.")
    return atp

def update_platform(platforms: list) -> list:
    selected_platforms = []
    while True:
        option = get_int("Seleccione la o las plataformas donde se encuentra disponible\n1. Neflix\n2. Disney+\n3. Star+\n4. Prime video\n",min=1,max=4)
        if platforms[option - 1] not in selected_platforms:
            selected_platforms.append(platforms[option - 1])
        else:
            print(f"{platforms[option - 1]} ya se encuentra en la lista.")
        if not get_confirm("¿Agregar más plataformas? [S/n]: "):
            break

    return selected_platforms