class movies():
    def __init__(self, arrayOfMovies):
        self.movies = arrayOfMovies

    def allMovies(self):
        '''Returns all Movies'''
        return self


class movie():
    def __init__(self, name):
        self.name = name

    def newItem(self):
        return self




alles = movies.allMovies('abc')

print(alles)