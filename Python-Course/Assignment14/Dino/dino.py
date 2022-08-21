import arcade
from time import sleep
class Dino(arcade.Sprite):
    def __init__(self):
        super().__init__()
        # self.cur_texture = 0
        self.texture = arcade.load_texture("./imgs/dino-walk-0.png")
        self.cower = False
        self.jumping = False  
        self.walking = True 
        self.scale = 0.3
        self.center_x = 100
        self.center_y = 135
        self.speed = 5
        self.fr = 0
    def update_animation(self, delta_time: float = 1 / 60):
        if self.fr > 15 and self.walking == True:  
            self.texture =  arcade.load_texture(f"imgs/dino-walk-0.png")
        elif self.fr > 0 and self.fr < 15 and self.walking == True:
            self.texture = arcade.load_texture(f"imgs/dino-walk-1.png")
        if self.fr > 15 and self.cower == True:  
            self.texture =  arcade.load_texture(f"imgs/dino-down-0.png")
            self.center_y = 120
        elif self.fr > 0 and self.fr < 15 and self.cower == True:
            self.texture = arcade.load_texture(f"imgs/dino-down-1.png")
            self.center_y = 120            
                  
    def impact(self):
        pass
        
    def duck(self):
        self.walking = False
        self.cower = True
        
    def walk(self):
        self.walking = True
        self.cower = False
        # self.center_y = 135    
    def jump(self):
        self.jumping = True                