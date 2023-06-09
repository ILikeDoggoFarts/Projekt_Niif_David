import pygame
def change_screen():
    # Clear the screen
    screen.fill((0, 0, 0))

    # Create the new screen text
    new_screen_text = "New Screen"
    new_screen_text_surface = font.render(new_screen_text, True, (255, 255, 255))

    # Calculate the position of the new screen text
    new_screen_text_x = screen_width // 2 - new_screen_text_surface.get_width() // 2
    new_screen_text_y = screen_height // 2 - new_screen_text_surface.get_height() // 2

    # Draw the new screen text
    screen.blit(new_screen_text_surface, (new_screen_text_x, new_screen_text_y))

    # Update the display
    pygame.display.flip()
