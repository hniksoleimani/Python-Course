class Media():
    def __init__(self, d, n, dir, I, u, dure, c, cs, y):
        self.ID = d
        self.name = n 
        self.director = dir
        self.IMDB_score = I 
        self.url = u
        self.duration = dure 
        self.cast = c
        self.casts = cs
        self.year = y
    def showInfo(self):
        print(f'ID\t{self.ID}')
        print(f'Name:\t{self.name}')
        print(f'Director name:\t{self.director}')
        print(f'IMDB_score:\t{self.IMDB_score}')
        print(f'Duration:\t{self.duration}')
        print(f'Cast:\t{self.cast}')
        print(f'Year:\t{self.year}')
        print(f'Genre:\t{self.year}')

    def add_media(self):
        pass

    def edit_media(self):
        pass

    def search(self):
        pass

    def delete_media(self):
        pass

    def show_menu(self):
        pass