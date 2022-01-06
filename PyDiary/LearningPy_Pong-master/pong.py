#import modules
from uagame import Window
import time
import pygame, sys
from pygame.locals import *



#Define Canvas (Window)
def main():
    window = Window("Pong", 500, 400)
    window.set_auto_update(False)
    game = Game(window)
    game.play()
    
    window.close()
    
    
    
#Game Frame
class Game:

    def __init__(self, window):
        self.window = window
        self.bg_color = pygame.Color('black')
        self.pause_time = 0.01 #frame rate
        self.close_clicked = False
        self.continue_game = True
        surface = window.get_surface()
        ball_color = 'white'
        ball_radius = 5
        ball_center = [250, 200]
        ball_velocity = [3,1]
        self.ball = Ball(ball_color, ball_radius, ball_center, ball_velocity, surface)
        self.paddle1=Paddle(70,surface)
        self.paddle2=Paddle(430, surface)        
        

    def play(self):
        while not self.close_clicked:
            self.handle_event()
            self.draw()
            
            
            if self.continue_game:
                self.update()
                self.decide_continue()
                
                
            time.sleep(self.pause_time)
    
        
        
        
    #Not sure how this works
    
    def handle_event(self):
        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True
            
            
            
    def draw(self):
        self.window.clear()
        self.ball.draw()
        surface =self.window.get_surface()
        self.paddle1.draw()
        self.paddle2.draw()
        self.window.update()

    def update(self):
        self.ball.move()
        if self.ball.velocity[0]>0:
            coords=[self.ball.center[0]+self.ball.radius,self.ball.center[1]]
        if self.ball.velocity[0]<0:
            coords=[self.ball.center[0]-self.ball.radius,self.ball.center[1]]            
        if self.paddle1.checkcollision(coords,"L") and self.ball.velocity[0]<0:
            self.ball.velocity[0] *=-1
        if self.paddle2.checkcollision(coords,"R")and self.ball.velocity[0]>0:
            self.ball.velocity[0] *=-1           
        
    
    def decide_continue(self):
        pass 

#The Ball
class Ball:
    def __init__(self, color, radius, center, velocity, surface):
        self.color = pygame.Color(color)
        self.radius = radius
        self.center = center
        self.velocity = velocity
        self.surface = surface
            
        
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
        
            
        
    def move(self): 
        paddle_height = 40
        paddle_width = 10
        paddle1_x = 70
        paddley = 180
        paddle2_x = 415
        paddle_y_position = (180, 220)
       
        
        size = self.surface.get_size()
        for coord in range(0,2):
            self.center[coord] = (self.center[coord] + self.velocity[coord])          
            if self.center[coord] < self.radius :
                self.velocity[coord] = -self.velocity[coord]
            if self.center[coord] + self.radius > size[coord]:
                self.velocity[coord] = -self.velocity[coord]
            
             
                
#Paddle Varible                
class Paddle: 
    def __init__(self, x_coords, surface):
        self.paddle_height = 40
        self.surface = surface
        self.paddle_width = 10
        self.paddle_x = x_coords
        self.paddle_y = 180
        self.WHITE=(255,255,255)  
        self.paddle=pygame.Rect(self.paddle_x, self.paddle_y, self.paddle_width,self.paddle_height)
        
    def draw(self):
        #pygame.draw.rect(surface, WHITE, (self.paddle_x, self.paddle_y, self.paddle_width,self.paddle_height))
        pygame.draw.rect(self.surface, self.WHITE, self.paddle)
        
    def checkcollision(self,coords,side):
        if side=="R":
            if abs(self.paddle.right-coords[0])<15 and (self.paddle.bottom>coords[1] and coords[1]>self.paddle.top):
                return True
            else: return False
        else:
            if abs(self.paddle.left-coords[0])<15  and (self.paddle.bottom>coords[1] and coords[1]>self.paddle.top):
                return True
            else: return False

main()
