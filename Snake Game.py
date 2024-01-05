import pygame
import random
import math

#Constants
width = 640
height = 640
pixels = 32
squares = int(width / pixels)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
score_value = 0
text_x_coord = 240
text_y_coord = 5

#Colors
BG1 = (156, 210, 54)
BG2 = (147, 203, 57)

#Player Specifications
player_pos_x = 640 / 2
player_pos_y = 640 / 2
player_vel_x = 0
player_vel_y = 0
movement_speed = 200

#Food Specifications
food_pos_x = random.randrange(0, 640 - pixels, 32)
food_pos_y = random.randrange(0, 640 - pixels, 32)

#Pygame Setup
pygame.init()
running = True
dt = 0

#Draw Background
def draw(screen):
    screen.fill(BG1)
    counter = 0
    for row in range(squares):
        for col in range(squares):
            if counter % 2 == 0:
                pygame.draw.rect(screen, BG2, (col * 32, row * 32, 32, 32))
            if col == squares - 1:
                continue
            counter += 1
            
#Draw Scoreboard           
def draw_score(text_x_coord, text_y_coord):
    font = pygame.font.Font("freesansbold.ttf", 32)
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (text_x_coord, text_y_coord))

#Draw/Randomize Food spawn           
def spawn_food(food_pos_x, food_pos_y):
    pygame.draw.rect(screen, "red", [(food_pos_x, food_pos_y), (32, 32)])

#Game program loop -----------------------------------------------------------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
 #Draw Background 
    draw(screen)         
  
#Draw Player Snake
    player_head = pygame.draw.rect(screen, "black", [(player_pos_x, player_pos_y), (32,32)])
    
 #Movement   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_vel_x = 0
        player_vel_y = -movement_speed * dt
        current_direction = "UP"
    if keys[pygame.K_s]:
        player_vel_x = 0
        player_vel_y = movement_speed * dt
        current_direction = "DOWN"
    if keys[pygame.K_a]:
        player_vel_y = 0
        player_vel_x = -movement_speed * dt
        current_direction = "LEFT"
    if keys[pygame.K_d]:
        player_vel_y = 0
        player_vel_x = movement_speed * dt
        current_direction = "RIGHT"
#Movement Update(s)   
    player_pos_x += player_vel_x
    player_pos_y += player_vel_y
             
#Boundaries       
    if(player_pos_x <= 0):
        player_pos_x = 0
    elif(player_pos_x >= 608):
        player_pos_x = 608
               
    if(player_pos_y <= 0):
        player_pos_y = 0
    elif(player_pos_y >= 608):
        player_pos_y = 608
        
#Food
    spawn_food(food_pos_x, food_pos_y)
    distance_head_food = math.sqrt(pow(food_pos_x - player_pos_x, 2) + pow(food_pos_y - player_pos_y, 2))
    if distance_head_food < 10:
        score_value += 1
        draw(screen)
        food_pos_x = random.randrange(0, 640 - pixels, 32)
        food_pos_y = random.randrange(0, 640 - pixels, 32)
        spawn_food(food_pos_x, food_pos_y)
                  
#Scoreboard
    draw_score(text_x_coord, text_y_coord)
   
#Update Screen
    pygame.display.flip()

#Delta Time
    dt = clock.tick(60) / 1000

pygame.quit()