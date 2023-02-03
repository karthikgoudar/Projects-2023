import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("Binary Search Visualization")

# List of bars with random heights
bars = [random.randint(10, 550) for _ in range(300)]

# Color of the bars
bar_color = (255, 255, 255)

# Color of the background
background_color = (0, 0, 0)

# Width of each bar
bar_width = 2

# Space between each bar
bar_space = 4

# Speed of sorting
sort_speed = 2

# Initialize the clock
clock = pygame.time.Clock()

# Find the target value to be searched in the list
target = random.choice(bars)

# Variable to store the current search range
left = 0
right = len(bars) - 1

# Loop until the user clicks the close button
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(background_color)

    # Draw the bars
    for i in range(len(bars)):
        color = bar_color
        if left <= i <= right:
            color = (255, 0, 0)
        pygame.draw.rect(screen, color, [i * (bar_width + bar_space), 600 - bars[i], bar_width, bars[i]])

    # Perform binary search
    if left <= right:
        mid = (left + right) // 2
        if target == bars[mid]:
            left = right + 1
        elif target < bars[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Update the screen
    pygame.display.flip()

    # Set the clock speed
    clock.tick(sort_speed)

# Quit Pygame
pygame.quit()
sys.exit()
