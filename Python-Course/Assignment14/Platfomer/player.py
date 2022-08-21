import arcade

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()

        # self.texture = arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")

        self.stand_right_textures =[arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")]
        
        self.stand_left_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")]
        
        self.walk_left_textures = [
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png", mirrored = True)
        # arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk8.png", mirrored = True)
        ]
        
        self.walk_right_textures = [
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png"),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png"),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png"),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png"),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png"),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png"),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png"),
        arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png")
        # arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk8.png")
        ]
        


        self.center_x = 200
        self.center_y = 100
        self.lives = 3
        self.score = 0
        self.pocket = []
        self.speed = 5
    def impact(self):
        self.score += 1
        # self.explosion = Explosion()
        # arcade.play_sound(arcade.sound.Sound(':resources:sounds/explosion1.wav'), 1.0, 0.0, False, 1.0)

