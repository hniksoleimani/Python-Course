import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")
        self.center_x = 200
        self.center_y = 100
        self.lives = 3
        self.score = 0

        self.speed = 5
    def impact(self):
        self.score += 1
        # self.explosion = Explosion()
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/explosion1.wav'), 1.0, 0.0, False, 1.0)




