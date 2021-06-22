import pygame
import random 
import abc
import math
from pygame import mixer
## set up for play window and color
pygame.init()
width, height = 650,750
win = pygame.display.set_mode((width,height))

white = [255,255,255]
green = [0,255,0]
blue = [0,0,255]
class Ball:
    def __init__(self,x,y,radius,color):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__color = color

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getRadius(self):
        return self.__radius
    
    def getColor(self):
        return self.__color

    def getLoc(self):
        return (self.__x, self.__y)
    
    def setLoc(self,newX,newY):
        self.__x = newX 
        self.__y = newY 

    def setWidth(self,newW):
        self.__width = newW

    def setHeight(self,newH):
        self.__height = newH
    
    def setColor(self,newC):
        self.__color = newC

    def draw(self,surface):
        x,y = self.getLoc()
        circle = pygame.draw.circle(surface,self.getColor(),(int(x),int(y)),self.getRadius())
        

    def get_rect(self):
        x,y = self.getLoc()
        rect = (x-self.getRadius(),y-self.getRadius(),2*self.getRadius(),2*self.getRadius())
        return rect 

#Background image

#Background Sound 
#mixer.music.load('background.wav')
#-1 makes the music file play on loop
#mixer.music.play(-1)

#Sun image
sun_img = pygame.image.load('sun.png')
sun_x = width - 64
sun_y = 0

#Cloud Image
cloud_img = pygame.image.load('cloud.png')

def Cloud(x,y):
    win.blit(cloud_img,(x,y))

#PLayer image
player_img = pygame.image.load('ninja.png')      
player_x = 0
player_y = height - height//3 - 64 
change_player_x =  0
change_player_y = 0 
def Player(x,y):
    win.blit(player_img,(x,y))


#Enemy image
enemy_img = []
enemy_x = []
enemy_y = []
change_enemy_x = []
change_enemy_y = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('carnivorous-plant.png'))
    enemy_x.append(random.randint(0,width))
    enemy_y.append(height - height//3 - 64)
    change_enemy_x.append(0.1)
    change_enemy_y.append(0.1)


def Enemy(x,y,i):
    win.blit(enemy_img[i],(x,y))

#shuriken
#ready state - you can't see the shuriken on the screen
#fire - shuriken is currently moving
shuriken_img = pygame.image.load('shuriken.png') 
shuriken_x = player_x
shuriken_y = player_y
shuriken_x_change = 3
shuriken_y_change = 1
shuriken_state = "ready"

def shoot_shuriken(x,y):
    global shuriken_state
    shuriken_state = "fire"
    win.blit(shuriken_img,(x + 16,y + 10))

#Collision with shuriken and enemy
def collision(enemy_x,enemy_y,shuriken_x,shuriken_y):
    distance_form = math.sqrt((math.pow(enemy_x - shuriken_x,2)) + (math.pow(enemy_y - shuriken_y,2)))
    if distance_form < 27:
        return True
    else:
        return False

#Scoreboard
score_value = 0 
font = pygame.font.Font('freesansbold.ttf',32)
text_x = 10 
text_y = 10

def show_score(x,y):
    score = font.render("Score: " +str(score_value), True,(255,255,255))
    win.blit(score,(x,y))


#Game over text
game_over = pygame.font.Font('freesansbold.ttf',32)

def game_over_text():
    over_text = game_over.render("Game Over", True,(255,255,255))
    win.blit(over_text,(width//2,height//2))

#Game Loop
win.fill(green)
win.fill(blue,(0,0,width,height - height//4))
#ball = Ball(20,400,20,(255,0,0))
running = True

while running: 

    win.fill(green)
    win.fill(blue,(0,0,width,height - height//3))
    win.blit(sun_img,(sun_x,sun_y))
    Cloud(300,300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_player_x = -0.1
                print("left key")
            if event.key == pygame.K_RIGHT:
                change_player_x = 0.1
                print("right key")
            if event.key == pygame.K_UP:
                print("up key")
                change_player_y = -0.1
            if event.key == pygame.K_DOWN:
                print("down key")
                change_player_y = 0.1
            if event.key == pygame.K_SPACE:
                if shuriken_state is "ready":
                    #shuriken_sound = mixer.Sound('laser.wav')
                    #shuriken_sound.play()
                    #gets the y coordinate of the player and equates that 
                    # to the shuriken y so that it doesnt follow where the player goes
                    shuriken_y = player_y
                    print("space bar is pressed")
                    shoot_shuriken(shuriken_x,player_y)
            if event.key == pygame.K_a:
                print("A button is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key has been released")

    #checks to see if player hits boundaries of window and make sure it doesn't go out of bounds
    if player_x <= 0:
        player_x = 0
    elif player_x >= width-64:
        player_x = width - 64

    if player_y <= 0:
        player_y = 0
    elif player_y >= height - height//3 - 64:
        player_y = height - height//3 - 64

    #Enemies movement
    for i in range(num_of_enemies):
        #Game over condition
        """
        if enemy_x[i] < 0:
            for j in range(num_of_enemies):
                enemy_x[j] = -5
            game_over_text()
            break
        enemy_x[i] -= change_enemy_x[i]
        """
        """
        if enemy_x[i] <= 0:
            change_enemy_x[i] = 4 
            enemy_y[i] += change_enemy_y[i]
        elif enemy_x[i] >= height:
            change_enemy_x[i] = -4
            enemy_y[i] += change_enemy_y[i]
        """
        #Collision
        collide = collision(enemy_x[i],enemy_y[i],shuriken_x,shuriken_y)
        if collide:
            #collide_sound = mixer.Sound('laser.wav')
            #collide_sound.play()
            shuriken_x = player_x
            shuriken_state = "ready"
            score_value += 1
            print(score_value)
            #generates another enemy once the one is taken out
            enemy_x[i]=random.randint(0,width)
            enemy_y[i]=height - height//3 - 64 

        Enemy(enemy_x[i],enemy_y[i],i)
    #Shuriken mechanics
    if shuriken_x >= width:
        shuriken_x = 0
        shuriken_state = "ready"
    if shuriken_state is "fire":
        shoot_shuriken(shuriken_x,player_y)
        #shuriken_y -= shuriken_y_change
        shuriken_x += shuriken_x_change


    

    player_y += change_player_y
    player_x += change_player_x
    Player(player_x,player_y)

    show_score(text_x,text_y)

    
    
    pygame.display.update()

        





