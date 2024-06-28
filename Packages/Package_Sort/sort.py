from movie.class_movies import Movies

def bubble_sort_title(movies: Movies, upward = True):
    films = movies.get_movies()
    for i in range(len(films)-1,-1,-1):
        for j in range(0,i):
            bigger = films[j+1]
            lower = films[j]
            if films[j].get_title() > films[j+1].get_title():
                bigger = films[j]
                lower = films[j+1]
            if upward:
                films[j],films[j+1] = lower, bigger
            else:
                films[j],films[j+1] = bigger, lower
                
def bubble_sort_genre(movies: Movies, upward = True):
    films = movies.get_movies()
    for i in range(len(films)-1,-1,-1):
        for j in range(0,i):
            bigger = films[j+1]
            lower = films[j]
            if films[j].get_genre() > films[j+1].get_genre():
                bigger = films[j]
                lower = films[j+1]
            if upward:
                films[j],films[j+1] = lower, bigger
            else:
                films[j],films[j+1] = bigger, lower

def bubble_sort_year(movies: Movies, upward = True):
    films = movies.get_movies()
    for i in range(len(films)-1,-1,-1):
        for j in range(0,i):
            bigger = films[j+1]
            lower = films[j]
            if films[j].get_year() > films[j+1].get_year():
                bigger = films[j]
                lower = films[j+1]
            if upward:
                films[j],films[j+1] = lower, bigger
            else:
                films[j],films[j+1] = bigger, lower

def bubble_sort_duration(movies: Movies, upward = True):
    films = movies.get_movies()
    for i in range(len(films)-1,-1,-1):
        for j in range(0,i):
            bigger = films[j+1]
            lower = films[j]
            if films[j].get_length() > films[j+1].get_length():
                bigger = films[j]
                lower = films[j+1]
            if upward:
                films[j],films[j+1] = lower, bigger
            else:
                films[j],films[j+1] = bigger, lower