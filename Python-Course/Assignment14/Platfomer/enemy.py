import arcade
import random 
class Enemy(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()

        # self.texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        # self.texture = arcade.load_texture(":resources:images/tiles/bomb.png")
        self.stand_right_textures =[arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")]
        
        self.stand_left_textures = [arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")]
        
        self.walk_left_textures = [
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk1.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk2.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk3.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk4.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk5.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk6.png", mirrored = True),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk7.png", mirrored = True)
        # arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk8.png", mirrored = True)
        ]
        
        self.walk_right_textures = [
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk0.png"),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk1.png"),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk2.png"),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk3.png"),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk4.png"),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk5.png"),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk6.png"),
        arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk7.png")
        # arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk8.png")
        ]        
        self.center_x = random.randint(0, 700)
        self.center_y = 600
        self.speed = 4
        self.change_x = random.choice([-1,1])
    # def move(self):
    #     self.center_y -=self.speed
