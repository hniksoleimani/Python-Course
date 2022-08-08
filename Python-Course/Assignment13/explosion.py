import arcade

class Explosion(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./exp_resized.png")
        self.width = 200
        self.height = 200
        self.center_x = x
        self.center_y = y