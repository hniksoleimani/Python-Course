from Media import Media
class Film(Media):
    def __init__(self, d, n, dir, I, u, dure, c, cs, y, g):
        Media.__init__(self, d, n, dir, I, u, dure, c, cs, y)
        self.genre = g