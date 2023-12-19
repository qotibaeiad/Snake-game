import pygame
import sys
import random
import math
import time


class Node:
    def __init__(self, x, y, color):
        self.x_position = x
        self.y_position = y
        self.color = color
        self.tmp = 0
        self.next = None

    def prepend(self, x, y, color):
        new_node = Node(x, y, color)
        new_node.next = self.head
        self.head = new_node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, x, y, color):
        new_node = Node(x, y, color)
        new_node.next = self.head
        self.head = new_node

    def delete(self, x, y, color):
        if self.is_empty():
            return

        if self.head.x_position == x and self.head.y_position == y:
            self.head = self.head.next
            return

        current = self.head
        while current.next and (current.next.x_position != x or current.next.y_position != y or current.next.color != color):
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.x_position, end=" -> ")
            current = current.next
        print("None")


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def create_node(x, y, color):
    return {"rect": pygame.Rect(x, y, 20, 20), "color": color, "next": None}


def draw_rectangle(screen, rect, color):
    pygame.draw.rect(screen, color, rect)


# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")
score_variable=0
#Text
pygame.font.init()
font = pygame.font.Font(None, 36)
# Create a text surface
score_text = font.render("Score: {}".format(score_variable), True, (255, 1, 1))  # Adjust the color as needed

# Get the rect object from the text surface
text_rect = score_text.get_rect()

# Set the position of the text 
text_rect.topleft = (10, 10)

# Blit the text surface onto the screen
screen.blit(score_text, text_rect)
# Initialize variables
linked_list = LinkedList()
pos_x, pos_y = 200, 200
rect_color = (0, 128, 255)
linked_list.prepend(200, 200, rect_color)
random_rec_color = (255, 0, 0)
rect_size = (20, 20)
max_distance = calculate_distance(20, 20, 40, 40)

# Initialize x and y
x, y = random.randint(0, 780), random.randint(0, 580)
while x%20!=0 or y%20!=0:
    x, y = random.randint(0, 780), random.randint(0, 580)
dis = calculate_distance(pos_x, pos_y, x, y)

# Main game loop
running = True
speed = 20
# Flags to indicate movement direction
moving_up = False
moving_down = False
moving_left = False
moving_right = True
cnt=0
# Event loop
while running:
    time.sleep(0.07)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check for key presses
            moving_up, moving_down, moving_left, moving_right = False, False, False, False
            if event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True

    # Update position based on movement flags
    if dis >= max_distance:
        if moving_up and pos_y > 0:
            current = linked_list.head
            while current:
                if current.next:
                    current.x_position = current.next.x_position
                    current.y_position = current.next.y_position 
                else:
                    current.y_position -= speed
                current = current.next
            pos_y -= speed
        elif moving_down and pos_y + rect_size[1] < height:
            current = linked_list.head
            while current:
                if current.next:
                    current.y_position = current.next.y_position #- rect_size[1]
                    current.x_position = current.next.x_position
                else:
                    current.y_position += speed
                current = current.next
            pos_y += speed
        elif moving_left and pos_x > 0:
            current = linked_list.head
            while current:
                if current.next:
                    current.x_position = current.next.x_position
                    current.y_position = current.next.y_position
                else:
                    current.x_position -= speed
                current = current.next
            
            pos_x -= speed
        elif moving_right and pos_x + rect_size[0] < width:
            current = linked_list.head
            while current:
                if current.next:
                    current.x_position = current.next.x_position
                    current.y_position = current.next.y_position 

                else:
                    current.x_position += speed
                current = current.next
            pos_x += speed

    # Paint the screen
    screen.fill((255, 255, 255))

    # Draw rectangles
    rect_position = (pos_x, pos_y)
    #draw_rectangle(screen, pygame.Rect(rect_position, rect_size), rect_color)

    # Draw random rectangle
    dis = calculate_distance(pos_x, pos_y, x, y)

    while 0 < dis < max_distance:
        linked_list.prepend(pos_x,pos_y,rect_color)
        score_variable+=1
        pos1=linked_list.head
        print("----------------------------")
        while pos1:
            print(pos1.x_position,",",pos1.y_position)
            pos1=pos1.next
        print("----------------------------")
        x, y = random.randint(0, 780), random.randint(0, 580)
        while x%20!=0 or y%20!=0:
            x, y = random.randint(0, 780), random.randint(0, 580)
        dis = calculate_distance(pos_x, pos_y, x, y)
    random_rec = (x, y)
    draw_rectangle(screen, pygame.Rect(random_rec, rect_size), random_rec_color)

    current = linked_list.head
    while current:
        draw_rectangle(screen,pygame.Rect((current.x_position,current.y_position),rect_size),rect_color)
        current = current.next
    #print("None")
        linked_list.display


    score_text = font.render("Score: {}".format(score_variable), True, (255, 1, 1))
    screen.blit(score_text, text_rect)


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
