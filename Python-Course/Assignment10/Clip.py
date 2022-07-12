from Media import Media
class Clip(Media):
    def __init__(self, d, n, dir, I, u, dure, c, cs, y, f):
        Media.__init__(self, d, n, dir, I, u, dure, c, cs, y)
        self.format = f
