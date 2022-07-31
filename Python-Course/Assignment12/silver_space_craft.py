import math
import random
from time import time
import arcade
from time import sleep
from math import modf

EXPLOSION_TEXTURE_COUNT = 60


class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 48
        self.height = 48
        self.score = 0
        self.center_x = w // 2
        self.center_y = 48 
        self.angle = 0
        self.lives = 3
        self.change_angle  = 0
        self.bullet_list = []
        self.speed = 4
    def rotate(self):
        self.angle += self.change_angle * self.speed
    def fire(self):
        self.bullet_list.append(Bullet(self))
        arcade.play_sound(arcade.sound.Sound(":resources:sounds/hurt5.wav"), 1.0, 0.0, False, 1.0)
    def impact(self):
        self.score += 1
        # self.explosion = Explosion()
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/explosion1.wav'), 1.0, 0.0, False, 1.0)

            
class Explosion(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("./exp_resized.png")
        self.width = 200
        self.height = 200
        self.center_x = x
        self.center_y = y
        
class Life(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(":resources:images/space_shooter/playerLife1_orange.png")
        self.width = 20
        self.height = 20
        self.center_x = x
        self.center_y = y  
    
        
class Enemy(arcade.Sprite):
    def __init__(self, w , h, s):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.speed = s
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.angle = 180
        self.width = 48
        self.height = 48
    def move(self):
        self.center_y -=self.speed
        



class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed = 20
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y

    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

    
class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        self.s = 4
        arcade.Window.__init__(self, width =  self.w, height = self.h, title = 'Silver Spacecraft', antialiasing = True)
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:/images/backgrounds/stars.png")
        self.player_life_list = []
        self.me = SpaceCraft(self.w, self.h)
        self.enemy_list = []
        self.start_time = time()
        self.start = time()
        self.explosion_list = []
        self.life = Life(30,30)
        
        self.textOver = 'GAME OVER'
        # self.x = 50
        # self.y = 50
        # self.x_score = 650
        # self.y_score = 30
        self.x2 = self.w // 3
        self.y2 = self.h // 3
        self.color = arcade.color.WHITE
        self.size2 = 34
        # self.ss = 15
        # self.size = 12
        x = 0
        for i in range(self.me.lives):
            self.player_life_list.append(Life(30+x, 30))
            x += 20
        self.speed = 10    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f'Score:{modf(self.me.score)[1]}', 650, 30, self.color, 12)
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
        self.me.draw()
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()
        for i in range(len(self.player_life_list)):
            self.player_life_list[i].draw()
        
        for i in range(len(self.enemy_list)):
            for j in range(len(self.me.bullet_list)):     
                if arcade.check_for_collision(self.enemy_list[i], self.me.bullet_list[j]):
                    Explosion(self.enemy_list[i].center_x, self.enemy_list[i].center_y).draw()
                    # self.me.explosion.draw()
                    self.enemy_list[i].remove_from_sprite_lists()
                    self.me.bullet_list[j].remove_from_sprite_lists()
            
        if len(self.player_life_list) == 0:
            arcade.draw_text(self.textOver, self.x2, self.y2, self.color, self.size2)
            sleep(1)

    def on_update(self, delta_time):
        arcade.start_render()
        self.end_time = time()
        self.end = time()
        self.me.rotate()
        
        for i in range(len(self.me.bullet_list)):     
            self.me.bullet_list[i].move()
           
        if self.end_time - self.start_time >= random.randint(2,5): 
           self.enemy_list.append(Enemy(self.w, self.h, self.s))
           self.start_time = time()
           
        for i in range(len(self.enemy_list)):
            if self.end - self.start >= 10:
                self.s += 4
                self.start = time()
            self.enemy_list[i].move()        


        for i in self.enemy_list:
            for j in self.me.bullet_list:     
                if arcade.check_for_collision(i, j):
                    self.me.impact()
                    self.enemy_list.remove(i)
                    self.me.bullet_list.remove(j)
        for enemy in self.enemy_list:
            if enemy.center_y < -10:
                self.enemy_list.remove(enemy)
                self.player_life_list.pop(-1)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.me.change_angle = -1
        elif key == arcade.key.LEFT:
            self.me.change_angle = 1
        elif key == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, key, modifiers):
        self.me.change_angle = 0

game = Game()
arcade.run()

