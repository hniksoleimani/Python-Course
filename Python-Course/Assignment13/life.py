import arcade

class Life(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./heart_resized.png")
        self.width = 40
        self.height = 40
        self.center_x = x
        self.center_y = y  