[Link de youtube](https://youtu.be/Ua5soysHttk)

### Ejecutar el programa

- `python3 main.py` (Ejecuta el programa)

### Algunas funciones que me gustaría aclarar

- bubble_sort()

```python
def bubble_sort_title(array: list[Movie], upward = True):
    for i in range(len(array)-1,-1,-1):
        for j in range(0,i):
            bigger = array[j+1]
            lower = array[j]
            if array[j].get_title() > array[j+1].get_title():
                bigger = array[j]
                lower = array[j+1]
            if upward:
                array[j],array[j+1] = lower, bigger
            else:
                array[j],array[j+1] = bigger, lower
```

Este bubble sort guarda el valor de la posición actual y la siguiente en dos variables llamdas bigger y lower, dependiendo del parámetro upward, que eso se pasa como parámetro con un condicional, la función va a ordenar de forma ascendente o de forma descendente. Esto aplica para todos los bubble sort del módulo.

- genre_list()

```
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
```

En esta función, como yo desconozco cuales géneros existen en la lista de películas y cuales no, lo que hago es recorrer la lista de películas y si el género de cada posición, no se encuentra ya guardado en la lista 'genres' en la posición [i][0], hago un .append() con una lista de 2 posiciones, donde en la primera posición guardo el nombre del género y en la segunda posición lo declaro como 1 ya que es el primero, en el caso de que si se encuentre el género en la lista, le sumo 1 al contador del mismo.
