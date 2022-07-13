from Media import Media
class Documentary(Media):
    def __init__(self, d, n, dir, I, u, dure, c, cs, y, loc):
        Media.__init__(self, d, n, dir, I, u, dure, c, cs, y)
        self.location = loc