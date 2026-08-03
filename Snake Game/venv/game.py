import pygame
import random
import time

# Initialize game
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 700

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Main game loop
while True:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
                
    # Update direction
    if change_to == 'UP':
        direction = 'UP'
    elif change_to == 'DOWN':
        direction = 'DOWN'
    elif change_to == 'LEFT':   
        direction = 'LEFT'
    elif change_to == 'RIGHT':
        direction = 'RIGHT'
        
    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True
        
    # Game Over conditions
    if snake_body[0][0] < 0 or snake_body[0][0] > (WIDTH - 10):
        game_over()
    if snake_body[0][1] < 0 or snake_body[0][1] > (HEIGHT - 10):
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
            
    # Display
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Update the display
    pygame.display.update()
    
    # control game speed
    pygame.time.Clock().tick(10)