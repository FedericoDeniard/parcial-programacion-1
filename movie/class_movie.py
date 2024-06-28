class Movie:

    def __init__(self, id: int, title: str, genre: str, year: int, length: int, atp: bool, platform: list):
        self.id = id
        self.title = title
        self.genre = genre
        self.year = year
        self.length = length
        self.atp = atp
        self.platform = platform
    
    def get_id(self):
        return self.id
    def get_title(self):
        return self.title
    def get_genre(self):
        return self.genre
    def get_year(self):
        return self.year
    def get_length(self):
        return self.length
    def get_atp(self):
        return self.atp
    def get_platform(self):
        return self.platform
    
    def get_movie(self):
        movie = self.id,self.title,self.genre,self.year,self.length,self.atp,self.platform
        return movie
    
    def show_movie(self) -> str:
        atp = "No"
        if self.get_atp():
            atp = "Si"
        duration = f"{self.length} min"

        platforms = " - ".join(self.get_platform())

        movie_string = f"|{self.get_title():^32}|{self.get_genre():^20}|{self.get_year():^13}|{duration:^10}|{atp:^19}|{platforms:^40}|"
        return movie_string

    def get_movie_dict(self) -> dict:
        movie_dict = {"id": self.id,"title": self.title,"genre": self.genre, "year": self.year,"length": self.length, "atp": self.atp}
        return movie_dict #TODO Creo que esta función no se usa más
    
    def set_title(self, new_title: str):
        self.title = new_title
    
    def set_genre(self, new_genre: str):
        self.genre = new_genre
    
    def set_year(self, new_year: int):
        self.year = new_year
    
    def set_length(self, new_length: int):
        self.length = new_length
    
    def set_atp(self, new_atp: bool):
        self.atp = new_atp
    
    def set_platform(self, new_platform: list):
        self.platform = new_platform
    
    def update_movie(self, title: str, genre: str, year: int, length: int, atp: bool,platform: list):
        self.set_title(title)
        self.set_genre(genre)
        self.set_year(year)
        self.set_length(length)
        self.set_atp(atp)
        self.set_platform(platform)