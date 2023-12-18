import pygame
import sys

# Initialize Pygame
pygame.init()
# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")
rect_color = (0, 128, 255)  # RGB color tuple
rect_position = (200, 200)  # (x, y) position of the top-left corner
rect_size = (20, 20) 
# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #Logic game
    # 
    # 
    # 
    # 
    # Pint the screen
    screen.fill((255, 255, 255))  # Fill the screen with white color

    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))






    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()