from movie.class_movie import Movie
import re
from Packages.Package_System.system import clear_screen
from Packages.Package_Input.Input import get_string, get_confirm, get_int
from Packages.Package_Crud.configs import new_id, save_id
from Packages.Package_Crud.update import update_atp,update_genre,update_length,update_title,update_year, update_platform

from datetime import datetime
class Movies:
    def __init__(self, path: str):
        self.movies: list[Movie] = []
        self.set_movies_from_file(path)
    
    def get_movies(self):
        return self.movies

    def new_movie(self, config: dict):
        clear_screen()
        id = new_id(config)
        title = get_string("Título: ",max_length=30,min_length=1)
        title = title.title()
        while not self.check_name_availability(title):
            print(f'La película "{title}" ya se encuentra cargada, ingrese una película diferente')
            title = get_string("Título: ",max_length=30,min_length=1)
            title = title.title()
        genre = get_string("Genero: ", max_length=18,min_length=1)
        genre = genre.capitalize()
        genres = config["genres"]
        while genre not in genres:
            print("Escriba un género válido \b")
            print(",".join(genres))
            genre = get_string("Genero: ", max_length=18,min_length=1)
            genre = genre.capitalize()
        actual_year = datetime.now().year
        year = get_int("Año de lanzamiento: ",error_message=f"El año debe estar entre 1888 y {actual_year}\n",min=1888,max= actual_year)
        length = get_int("Duración: ",min=0,max=999999999999999999999999)
        atp = get_confirm("¿Es apta para todo público? [S/n]\n ")
        platform = update_platform(config["platforms"])

        movie = Movie(id,title,genre,year,length,atp,platform)
        print(self.show_movies([movie]))
        if get_confirm():
            self.movies.append(movie)
            save_id(config,id)

    def delete_movie(self, title: str):
        clear_screen()
        movie = self.find_movie(title)
        if len(movie) > 0:
            movie = movie[0]
            while True:
                if get_confirm(f"La película siguiente película será eliminada\n{self.show_movies([movie])}\n¿Desea continuar? [S/n]\n"):
                    self.movies.remove(movie)    # TODO Acá podría cambiar a un pop para guardar la película eliminada en una lista si es necesario
                    break
                else:
                    print("Eliminación cancelada.")
                    break
        else:
            print(f"Película {title} no encontrada.")

    def update_movie(self, title: str, config: dict):
        clear_screen()
        genres = config["genres"]
        original_movie = self.find_movie(title)
        original_movie = original_movie[0]
        if original_movie!= None:
            movie_tuple = original_movie.get_movie()
            id, title, genre, year, length, atp, platform = movie_tuple
            copy_movie = Movie(id,title,genre,year,length, atp, platform)
            while True:
                clear_screen()
                print(self.show_movies([copy_movie]))
                option = get_int("¿Que desea modificar?\n1. Título\n2. Género\n3. Año de lanzamiento\n4. Duración\n5. ATP\n6. Plataformas\n7. Comparar cambios\n8. Guardar y salir\n9. Salir sin guardar\n",min=1,max=9)
                match option:
                    case 1:
                        copy_movie.set_title(update_title())
                    case 2:
                        copy_movie.set_genre(update_genre(genres))
                    case 3:
                        copy_movie.set_year(update_year())
                    case 4:
                        copy_movie.set_length(update_length())
                    case 5:
                        copy_movie.set_atp(update_atp())
                    case 6:
                        copy_movie.set_platform(update_platform(config["platforms"]))
                    case 7:
                        print(self.show_movies([original_movie,copy_movie]))
                    case 8:
                        print(self.show_movies([copy_movie]))
                        if get_confirm():
                            original_movie.update_movie(copy_movie.get_title(), copy_movie.get_genre(),copy_movie.get_year() ,copy_movie.get_length(),copy_movie.get_atp(), copy_movie.get_platform())
                            break
                    case 9:
                        if get_confirm("Los datos cargados se perderan\n¿Desea confirmar? [S/n]\n"):
                            break
                input("Presione una tecla para continuar...")
                clear_screen()
        else:
            print("Película no encontrada")

    def save_movies(self, path: str):
        with open(path, "w") as f:
            for movie in self.movies:
                id,title,genre,year,length,atp,platform = (movie.get_id(), movie.get_title(), movie.get_genre(), movie.get_year(), movie.get_length(), movie.get_atp(),movie.get_platform())
                platforms = " - ".join(movie.get_platform())
                f.write(f"{id},{title},{genre},{year},{length},{atp},{platforms}\n")
    
    def set_movies_from_file(self, path: str):
        with open(path, "r") as file:
            for line in file:
                movie = re.split(',|\n',line)
                if movie[5] == "True":
                    atp = True
                else:
                    atp = False
                
                platforms = movie[6].split("-")
                for i in range(len(platforms)):
                    platforms[i] = platforms[i].strip()
                movie = Movie(int(movie[0]), movie[1], movie[2], int(movie[3]),int(movie[4]),atp,platforms)
                self.movies.append(movie)

    def show_movies(self, list = None):
        clear_screen()
        message = []
        message.append("*" * 141)
        message.append(f"|{"Título":^32}|{"Género":^20}|{"Lanzamiento":^13}|{"Duración":^10}|{"Apto todo público":^19}|{"Plataformas":^40}|")
        message.append("-" * 141)
        if list == None:
            for movie in self.get_movies():
                message.append(movie.show_movie())
        else:
            for movie in list:
                message.append(movie.show_movie())
        message.append("*" * 141)
        message = "\n".join(message)
        return message

    def find_movie(self,find: str):
        found_movie = []
        for movie in self.movies:
            if movie.get_title() == find:
                found_movie.append(movie)
                break
        return found_movie
    
    def find_platform(self, find: str):
        found_movie = []
        for movie in self.movies:
            if find in movie.get_platform():
                found_movie.append(movie)
        return found_movie
    
    def find_genre(self, find: str):
        found_movie = []
        for movie in self.movies:
            if find == movie.get_genre():
                found_movie.append(movie)
        return found_movie
    
    def find_year(self, find: int):
        found_movie = []
        for movie in self.movies:
            if find == movie.get_year():
                found_movie.append(movie)
        return found_movie
    
    def find_atp(self, atp: bool):
        found_movie = []
        for movie in self.movies:
            if atp == movie.get_atp():
                found_movie.append(movie)
        return found_movie

    def length_average(self):
        total_length = 0
        for movie in self.movies:
            total_length += movie.get_length()
        average = total_length / len(self.movies)
        message = f"La duración promedio de las películas es: {average:.0f} minutos"
        return message
    
    def movies_after(self, year: int):
        movies_after_year = []
        for movie in self.movies:
            if movie.get_year() >= year:
                movies_after_year.append(movie)
        return movies_after_year

    def genre_list(self) -> list:
        genres = []
        for i in range(len(self.movies)):
            genre = self.movies[i].get_genre()
            found = False
            for j in range(len(genres)):
                if genres[j][0] == genre:
                    genres[j][1] += 1
                    found = True
                    break
            if not found:
                genres.append([genre, 1])
        return genres
    
    def atp_list(self) -> list:
        atp = [["Apto para todo público",0],["No apto para todo público", 0]]
        for i in range(len(self.movies)):
            if self.movies[i].get_atp() == True:
                atp[0][1] += 1
            else:
                atp[1][1] += 1
        return atp

    def show_percentage(self,list: list) -> str:
        clear_screen()
        message = []
        for movie in list:
            genre = movie[0]
            percentage = (movie[1] / len(self.movies)) * 100
            message.append(f"{genre}: {percentage:.0f}%")
        message = "\n".join(message)
        return message
    
    def check_name_availability(self, title: str) -> bool:
        is_available = True
        for movie in self.movies:
            if movie.get_title() == title:
                is_available = False
                break
        return is_available