from Media import Media
class Series(Media):
    def __init__(self, d, n, dir, I, u, dure, c, cs, y, s):
        Media.__init__(self, d, n, dir, I, u, dure, c, cs, y)
        self.numberOfSeasons = s 
