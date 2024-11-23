import pygame

pygame.init()

# Set window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# BG
background_color = (255, 255, 255)

# Run game
running = True
while running:
    # Fill screen with BG
    screen.fill(background_color)

    # Draw red rect
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))

    # Update the display
    pygame.display.flip()

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
