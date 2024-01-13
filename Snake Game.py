import pygame
import random
import math

from snake import Snake

# Constants
width = 640
height = 640
pixels = 32
squares = int(width / pixels)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
score_value = 0
text_x_coord = 240
text_y_coord = 5

# Colors
BG1 = (156, 210, 54)
BG2 = (147, 203, 57)

# Food Specifications
food_pos_x = random.randrange(0, 640 - pixels, 32)
food_pos_y = random.randrange(0, 640 - pixels, 32)

# Pygame Setup
pygame.init()
running = True
dt = 0
snake = Snake()  # Create Snake instance

# Draw Background
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

# Draw Scoreboard
def draw_score(text_x_coord, text_y_coord):
    font = pygame.font.Font("freesansbold.ttf", 32)
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (text_x_coord, text_y_coord))

# Draw/Randomize Food spawn
def spawn_food(food_pos_x, food_pos_y):
    pygame.draw.rect(screen, "red", [(food_pos_x, food_pos_y), (32, 32)])

# Game program loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw Background
    draw(screen)

    # Draw Player Snake
    player_head = pygame.draw.rect(screen, "black", [(snake.x, snake.y), (20, 20)])

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.vel_x = 0
        snake.vel_y = -snake.movement_speed * dt
    if keys[pygame.K_s]:
        snake.vel_x = 0
        snake.vel_y = snake.movement_speed * dt
    if keys[pygame.K_a]:
        snake.vel_y = 0
        snake.vel_x = -snake.movement_speed * dt
    if keys[pygame.K_d]:
        snake.vel_y = 0
        snake.vel_x = snake.movement_speed * dt

    # Movement Updates
    snake.x += snake.vel_x
    snake.y += snake.vel_y


    # Boundaries
    if snake.x <= 0:
        pygame.quit()
    elif snake.x >= 632:
        pygame.quit()
    if snake.y <= 0:
        pygame.quit()
    elif snake.y >= 640:
        pygame.quit()

    # Food
    spawn_food(food_pos_x, food_pos_y)
    distance_head_food = math.sqrt((food_pos_x - snake.x) ** 2 + (food_pos_y - snake.y) ** 2)
    if distance_head_food < 30:
        score_value += 1
        food_pos_x = random.randrange(0, 640 - pixels, 32)
        food_pos_y = random.randrange(0, 640 - pixels, 32)
        spawn_food(food_pos_x, food_pos_y)
        snake.movement_speed += 10

    # Scoreboard
    draw_score(text_x_coord, text_y_coord)

    # Update Screen
    pygame.display.flip()

    # Delta Time
    dt = clock.tick(60) / 1000

pygame.quit()