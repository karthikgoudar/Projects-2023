'''

Author : Karthik Goudar
date   : 2 Feb 2023


Bubble Sort Visualizer Using Pygame

'''

import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 480
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Variables for sorting
numbers = [random.randint(0, HEIGHT) for i in range(WIDTH // 10)]
sorted = False

# Bubble sort algorithm
def bubble_sort(numbers):
    global sorted
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                draw(numbers)
    sorted = True

# Function to draw the numbers
def draw(numbers):
    window.fill((255, 255, 255))
    for i, number in enumerate(numbers):
        pygame.draw.rect(window, (0, 0, 0), (i * 10, HEIGHT - number, 8, number))
    pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not sorted:
        bubble_sort(numbers)

    draw(numbers)
    time.sleep(20)
