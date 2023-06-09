import pygame
import os

# Get the current working directory
current_dir = os.getcwd()

# Specify the path to the background image file
image_filename = "ai.jpg"
image_path = os.path.join(current_dir, image_filename)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smash Bros")

# Load background image
background_image = pygame.image.load(image_path)

# Set up the font
font = pygame.font.Font(None, 64)

# Create the title text
title_text_surface = font.render("Smash Bros", True, (255, 0, 255))
title_text_width = title_text_surface.get_width()
title_text_height = title_text_surface.get_height()

# Create the "Press enter to continue" text
press_enter_text_surface = font.render("Press enter to continue", True, (255, 255, 255))
press_enter_text_width = press_enter_text_surface.get_width()
press_enter_text_height = press_enter_text_surface.get_height()

# Calculate the position of the title text surface
title_text_x = screen_width // 2 - title_text_width // 2
title_text_y = screen_height // 12 - title_text_height // 2

# Calculate the position of the "Press enter to continue" text surface
press_enter_text_x = screen_width // 2 - press_enter_text_width // 2
press_enter_text_y = screen_height // 2 - press_enter_text_height // 2

# Main loop
running = True
show_press_enter_text = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Enter key is pressed, do something
                print("Enter key is pressed!")
    
    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the title text
    screen.blit(title_text_surface, (title_text_x, title_text_y))

    # Show the "Press enter to continue" text every second
    if pygame.time.get_ticks() % 2000 < 1000:
        show_press_enter_text = True
    else:
        show_press_enter_text = False

    # Draw the "Press enter to continue" text if required
    if show_press_enter_text:
        screen.blit(press_enter_text_surface, (press_enter_text_x, press_enter_text_y))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
