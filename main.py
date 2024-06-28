'''
Nombre: Federico
Apellido: Deniard
'''
from Packages.Package_Crud.configs import load_config
from Packages.Package_Crud.configs import save_config
from Packages.Package_System.system import clear_screen
from Packages.Package_Input.Input import get_int,get_string
from Packages.Package_Sort.sort import bubble_sort_duration,bubble_sort_genre,bubble_sort_title,bubble_sort_year
from datetime import datetime

from movie.class_movies import Movies

def main():
    config_path = 'config.json'
    movies_path = 'films.csv'

    config = load_config(config_path)
    movies = Movies(movies_path)
    while True:
        clear_screen()
        option = get_int("1. Dar de alta\n2. Modificar\n3. Eliminar\n4. Mostrar películas\n5. Ordenar películas\n6. Buscar película por título\n7. Calcular\n8. Calcular porcentaje\n9. Salir\n",min=1,max=9)
        match option:
            case 1:
                movies.new_movie(config)
            case 2:
                if len(movies.get_movies()) == 0:
                    input("Debes tener cargada al menos 1 película para continuar...")
                else:
                    title = get_string("Ingrese el título de la película a modificar: ")
                    title = title.title()
                    movies.update_movie(title, config)
            case 3:
                if len(movies.get_movies()) == 0:
                    input("Debes tener cargada al menos 1 película para continuar...")
                else:
                    title = get_string("Ingrese el título de la película a buscar: ",max_length=30,min_length=1)
                    title = title.title()
                    movies.delete_movie(title)
            case 4:
                clear_screen()
                if len(movies.get_movies()) == 0:
                    input("Debes tener cargada al menos 1 película para continuar...")
                else:
                    show = get_int("1. Todas las películas\n2. De determinado género\n3. De determinado año\n4. Todas las ATP\n5. Todas las No ATP\n6. De determinada plataforma\n",min=1,max=6)
                    all_movies = False
                    match show:
                        case 1:
                            found = movies.show_movies()
                            all_movies = True
                        case 2:
                            genre = get_string("Genero: ", max_length=18,min_length=1)
                            genre = genre.capitalize()
                            while genre not in config["genres"]:
                                genre = get_string("Genero: ", max_length=18,min_length=1)
                                genre = genre.capitalize()
                            found = movies.find_genre(genre)
                        case 3:
                            actual_year = datetime.now().year
                            year = get_int("Año de lanzamiento: ",error_message=f"El año debe estar entre 1888 y {actual_year}\n",min=1888,max= actual_year)
                            found = movies.find_year(year)
                        case 4:
                            found = movies.find_atp(True)
                        case 5:
                            found = movies.find_atp(False)
                        case 6:
                            platform = get_string("Ingrese la plataforma a buscar: ",min_length=1, max_length=11)
                            platform = platform.capitalize()
                            found = movies.find_platform(platform)
                    if all_movies:
                        print(found)
                    elif len(found) > 0:
                        print(movies.show_movies(found))
                    else:
                        print("No se encontraron películas que cumplan con los criterios")
            case 5:
                if len(movies.get_movies()) == 0:
                    input("Debes tener cargada al menos 1 película para continuar...")
                else:
                    order = get_int("¿Por que parámetro desea ordenar?\n1. Título\n2. Género\n3. Año\n4. Duración\n",min=1,max=4)
                    upward = get_int("Ordenar de forma\n1. Ascendente\n2. Descendente\n",min=1,max=2)
                    upward_bool = upward == 1
                    match order:
                        case 1:
                            bubble_sort_title(movies,upward_bool)
                        case 2:
                            bubble_sort_genre(movies,upward_bool)
                        case 3:
                            bubble_sort_year(movies,upward_bool)
                        case 4:
                            bubble_sort_duration(movies,upward_bool)
            case 6:
                if len(movies.get_movies()) == 0:
                    input("Debes tener cargada al menos 1 película para continuar...")
                else:
                    title = get_string("Ingrese el título de la película a buscar: ",max_length=30,min_length=1)
                    title = title.title()
                    found_movie = movies.find_movie(title)
                    if len(found_movie) > 0:
                        print(movies.show_movies(found_movie))
                    else:
                        print("No se encontraron películas que cumplan con los criterios")
            case 7:
                if len(movies.get_movies()) == 0:
                    input("Debes tener cargada al menos 1 película para continuar...")
                else:
                    show = get_int("1. Duración promedio de todas las películas\n2. Cantidad de películas lanzadas en cada año desde 2005 hasta 2024\n")
                    match show:
                        case 1:
                            print(movies.length_average())
                        case 2:
                            print(movies.show_movies(movies.movies_after(2005)))
            case 8:
                if len(movies.get_movies()) == 0:
                    input("Debes tener cargada al menos 1 película para continuar...")
                else:
                    show = get_int("1. Porcentaje por género\n2. Porcentaje por ATP\n",min=1,max=2)
                    match show:
                        case 1:
                            genres = movies.genre_list()
                            print(movies.show_percentage(genres))
                        case 2:
                            atp = movies.atp_list()
                            print(movies.show_percentage(atp))
            case 9:
                movies.save_movies(movies_path)
                save_config(config_path,config)
                break
        input("Presione una tecla para continuar...")

main()