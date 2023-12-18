import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")

pos_x = 200
pos_y = 200
rect_color = (0, 128, 255)  # RGB color tuple
rect_position = (pos_x, pos_y)  # (x, y) position of the top-left corner
rect_size = (20, 20)

# Main game loop
running = True
speed = 0.09

# Flags to indicate movement direction
moving_up = False
moving_down = False
moving_left = False
moving_right = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True
        # Check for key releases
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_s:
                moving_down = False
            elif event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_d:
                moving_right = False

    # Update position based on movement flags
    if moving_up and  pos_y>0:
        pos_y -= speed
    if moving_down and pos_y<=height:
        pos_y += speed
    if moving_left and pos_x>0:
        pos_x -= speed
    if moving_right and pos_x<=width:
        pos_x += speed

    # Paint the screen
    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Update rectangle position
    rect_position = (pos_x, pos_y)

    # Draw the rectangle
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
