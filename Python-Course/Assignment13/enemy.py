import arcade
import random 
class Enemy(arcade.Sprite):
    def __init__(self, w , h):
        super().__init__()

        # self.texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.texture = arcade.load_texture(":resources:images/tiles/bomb.png")
        
        self.center_x = random.randint(0, 800)
        self.center_y = 600
        self.speed = 4
    def move(self):
        self.center_y -=self.speed
        





