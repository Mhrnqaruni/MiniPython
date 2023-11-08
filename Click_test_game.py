# This code is created by @Mhrnqaruni
# https://github.com/Mhrnqaruni/

import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 720, 720
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SQUARE_SIZE = 30

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font for the counter and timer
font = pygame.font.Font(None, 36)

# Initialize the counter and timer
counter = 0
start_time = None
elapsed_time = 0

# Function to draw a red square at a random location
def draw_square():
    x = random.randint(0, WIDTH - SQUARE_SIZE)
    y = random.randint(0, HEIGHT - SQUARE_SIZE)
    pygame.draw.rect(window, RED, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))
    return pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)

# Function to update the counter display
def update_counter():
    counter_text = font.render(str(counter), True, RED)
    window.blit(counter_text, (10, 10))

# Function to update the timer display
def update_timer():
    timer_text = font.render(str(elapsed_time), True, RED)
    window.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))

# Draw the initial square
square = draw_square()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if square.collidepoint(mouse_pos):
                window.fill(BLACK)
                square = draw_square()
                counter += 1
                if counter == 1:
                    start_time = time.time()
                elif counter == 10:
                    elapsed_time = time.time() - start_time

    update_counter()
    update_timer()
    pygame.display.flip()

pygame.quit()
