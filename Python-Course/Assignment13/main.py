from time import time
from time import sleep
import random
from math import modf

import arcade
from enemy import Enemy
from player import Player
from ground import Ground
from life import Life
from explosion import Explosion
class Game(arcade.View):
    def __init__(self):
        self.w = 800
        self.h = 600
        super().__init__()
        self.background_image = arcade.load_texture('background.jpg')
        self.gravity = 0.5
        self.life = Life(40,40)
        self.player_life_list = arcade.SpriteList()
        self.textOver = 'GAME OVER'
        self.x2 = 800 // 3
        self.y2 = 600 // 3
        self.color = arcade.color.WHITE
        self.size2 = 34
        self.me = Player()
        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()

        self.start_time = time()
        self.start = time()
        for i in range(0, 850, 120):
            ground = Ground(i, 40)
            self.ground_list.append(ground)
            
        x = 0
        for i in range(self.me.lives):
            self.player_life_list.append(Life(50+x, 50))
            x += 50
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, [self.ground_list, self.enemy_list],  gravity_constant = self.gravity)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f'Score:{modf(self.me.score)[1]}', 650, 30, self.color, 12)

        arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, self.background_image)

        self.me.draw()
        for ground in self.ground_list:
            ground.draw()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()
        for i in range(len(self.player_life_list)):
            self.player_life_list[i].draw()
            
            
        for j in range(len(self.enemy_list)):     
            if arcade.check_for_collision(self.enemy_list[j], self.me):
                Explosion(self.enemy_list[j].center_x, self.enemy_list[j].center_y).draw()
                self.me.explosion.draw()
                self.enemy_list[j].remove_from_sprite_lists() 
        if len(self.player_life_list) == 0:
            arcade.draw_text(self.textOver, self.x2, self.y2, self.color, self.size2)
            sleep(1)
                                 
    def on_update(self, delta_time: float):
        self.end_time = time()
    
               
        if self.end_time - self.start_time >= random.randint(2,5): 
           self.enemy_list.append(Enemy(self.w, self.h))
           self.start_time = time()   
               
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move() 
             
        for i in self.enemy_list:
            if arcade.check_for_collision(i, self.me):
                self.me.impact()
                self.enemy_list.remove(i)
                self.player_life_list.pop(-1)

        for enemy in self.enemy_list:
            if enemy.center_y < -10:
                self.enemy_list.remove(enemy)


        self.physics_engine.update()

    def on_key_press(self,key, modifiers):
        if key == arcade.key.LEFT:
            self.me.change_x = -1 * self.me.speed
        elif key == arcade.key.RIGHT:
            self.me.change_x = 1 * self.me.speed
        
        elif key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.me.change_y = 10

    def on_key_release(self, key, modifiers):
        self.me.change_x = 0




window = arcade.Window(800, 600, 'Platformer')

game = Game()

window.show_view(game)
arcade.run()