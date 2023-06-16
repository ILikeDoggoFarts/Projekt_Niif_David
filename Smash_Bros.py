import pygame

def change_screen(screen, font):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Create the new screen text
    new_screen_text = "Choose your character"
    new_screen_text_surface = font.render(new_screen_text, True, (255, 255, 255))

    # Calculate the position of the new screen text
    new_screen_text_x = screen_width // 2 - new_screen_text_surface.get_width() // 2
    new_screen_text_y = screen_height // 2 - new_screen_text_surface.get_height() // 2

    # Draw the new screen text
    screen.blit(new_screen_text_surface, (new_screen_text_x, new_screen_text_y))

    # Update the display
    pygame.display.flip()

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smash Bros")

# Load background image
background_image = pygame.image.load("ai.jpg")

# Set up the font
font = pygame.font.Font(None, 64)

# Create the title text
title_text_surface = font.render("Smash Bros", True, (255, 0, 255))

# Create the "Press enter to continue" text
press_enter_text_surface = font.render("Press enter to continue", True, (255, 255, 255))

# Calculate the position of the title text surface
title_text_x = screen_width // 2 - title_text_surface.get_width() // 2
title_text_y = screen_height // 12 - title_text_surface.get_height() // 2

# Calculate the position of the "Press enter to continue" text surface
press_enter_text_x = screen_width // 2 - press_enter_text_surface.get_width() // 2
press_enter_text_y = screen_height // 2 - press_enter_text_surface.get_height() // 2

# Flag to track the screen state
show_first_screen = True

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Enter key is pressed, switch screens
            show_first_screen = False

    if show_first_screen:
        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the title text
        screen.blit(title_text_surface, (title_text_x, title_text_y))

        # Show the "Press enter to continue" text every second
        if pygame.time.get_ticks() % 2000 < 1000:
            screen.blit(press_enter_text_surface, (press_enter_text_x, press_enter_text_y))
    else:
        # Call the function to switch screens
        change_screen(screen, font)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
