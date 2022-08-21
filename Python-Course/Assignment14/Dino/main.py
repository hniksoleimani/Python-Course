from time import time
from time import sleep
import random
from math import modf
import arcade

from dino import Dino
from ground import Ground, Box



class Cactus(arcade.AnimatedWalkingSprite):
    def __init__(self, s2):
        super().__init__()

        self.scale = 0.4
        self.fr = 0
        self.center_y = 125
        self.center_x = 800
        self.speed2 = s2
        # self.change_x = random.choice([-1,1])
        
    def update_animation(self, delta_time: float = 1 / 60):
        self.texture =  arcade.load_texture(f"imgs/cactus1_night.png")

             
    def move(self):
        self.center_x -=self.speed2
        
        
        
class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self, s1):
        super().__init__()

        self.scale = 0.4
        self.fr = 0
        self.center_y = random.randint(120, 250)
        self.center_x = 800
        self.speed = s1
        # self.change_x = random.choice([-1,1])
        
    def update_animation(self, delta_time: float = 1 / 60):
        if self.fr > 15 :  
            self.texture =  arcade.load_texture(f"imgs/bird0.png")
        elif self.fr > 0 and self.fr < 15 :
            self.texture = arcade.load_texture(f"imgs/bird1.png")   
             
    def move(self):
        self.center_x -=self.speed
        
        
class Game(arcade.View):
    def __init__(self):
        self.w = 800
        self.h = 600
        self.frame = 0
        self.score = 0
        super().__init__()
        self.gravity = 0.2
        self.textOver = 'GAME OVER'
        self.x2 = 800 // 3
        self.y2 = 600 // 3
        self.color = arcade.color.WHITE
        self.size2 = 34
        self.dino = Dino()
        self.s1 = 3
        self.s2 = 1
        self.ground_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.cactus_list = arcade.SpriteList()
        self.bird_start_time = 0
        self.bird_end_time = 0
        self.cactus_start_time = 0
        self.cactus_end_time = 0
        self.start1 = 0
        self.start2 = 4

        for i in range(0, 850, 120):
            ground = Ground(i, 40)
            self.ground_list.append(ground)

    def on_draw(self):
        arcade.start_render()

        self.dino.draw()

        # try:
        #     if arcade.check_for_collision(self.dino, self.key):
        #         self.me.pocket.append(self)
        #         del self.key
        #         print(len(self.me.pocket))
        # except:
        #     pass
        # if arcade.check_for_collision(self.dino, self.lock) and len(self.dino.pocket) > 0 :
        #     self.lock.texture = arcade.load_texture(":resources:images/items/flagGreen2.png")

        for ground in self.ground_list:
            ground.draw()

        for i in range(len(self.bird_list)):
            self.bird_list[i].draw()

        for j in range(len(self.bird_list)):     
            if arcade.check_for_collision(self.bird_list[j], self.dino):
                arcade.draw_text(self.textOver, self.x2, self.y2, self.color, self.size2)
                sleep(1)
        for i in range(len(self.cactus_list)):
            self.cactus_list[i].draw()

        for j in range(len(self.cactus_list)):     
            if arcade.check_for_collision(self.cactus_list[j], self.dino):
                arcade.draw_text(self.textOver, self.x2, self.y2, self.color, self.size2)
                sleep(1)           
            
            
            
        # if len(self.player_life_list) == 0:

        
        
        arcade.draw_text(f'Score:{modf(self.score)[1]}', 650, 50, self.color, 12)
                                 
    def on_update(self, delta_time: float = 1 / 60):
        self.end = time()
        
        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.dino, [self.ground_list],  gravity_constant = self.gravity)
        if self.score >= 5 :
            self.bird_end_time = time()
            if self.bird_end_time-self.bird_start_time >= random.randint(2,5):
                self.new_bird = Bird(self.s1)
                self.bird_list.append(self.new_bird)
                self.bird_start_time = time()   
            
        self.cactus_end_time = time()    
        if self.cactus_end_time-self.cactus_start_time >= random.randint(5,7):
            self.new_cactus = Cactus(self.s2)
            self.cactus_list.append(self.new_cactus)
            self.cactus_start_time = time()   
                       
        for j in range(len(self.bird_list)):     
            self.bird_list[j].move()
            
        for j in range(len(self.cactus_list)):     
            self.cactus_list[j].move()  
                                       
        for i in range(len(self.bird_list)):
            self.bird_list[i].update_animation()
            
        for i in range(len(self.cactus_list)):
            self.cactus_list[i].update_animation()
        # for bird in self.bird_list:
        #     if arcade.check_for_collision(bird, self.dino):
        #         self.dino.impact()
        #         pass
        #         self.bird_list.remove(i)
        #     if self.bird_list[i].center_x <= 0:
        #         self.bird_list[i].remove_from_sprite_lists()
        #         self.player_life_list.pop(-1)
                
        for k in range(len(self.bird_list)):
            if self.end - self.start1 >= 10:
                self.s1 += 2
                self.start1 = time()
            self.bird_list[k].move()
                  
        for l in range(len(self.cactus_list)):
            if self.end - self.start2 >= 10:
                self.s2 += 1
                self.start2 = time()
            self.cactus_list[l].move()    
                           
        for bird in self.bird_list:
            if bird.center_x < 0:
                self.bird_list.remove(bird)
                self.score += 5
                
        for cactus in self.cactus_list:
            if cactus.center_x < 0:
                self.cactus_list.remove(cactus)
                self.score += 1                

        self.my_physics_engine.update()

        
        
        self.frame += 1
        self.dino.fr = self.frame
        try:
            self.new_bird.fr = self.frame
            self.new_bird.move()
        except:
            pass
        if self.frame > 30:
            self.frame = 0
        self.dino.update_animation()                
    def on_key_press(self,key, modifiers):

        if key == arcade.key.DOWN:

            self.dino.duck()        
        if key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.dino.change_y = 8

    def on_key_release(self, key, modifiers):
        self.dino.change_x = 0
        self.dino.walk()    


window = arcade.Window(800, 600, 'Dino_walk')

game = Game()

window.show_view(game)
arcade.run()