
import pygame

pygame.init()

#Angaben zu den Bildschirmdimensionen
width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smash Bros")

weiss = [255, 255, 255]
schwarz = [0, 0, 0]
#Hintergrundbild
screen.fill(weiss)
#Schriftart
font = pygame.font.Font(None, 64)

#Titeltext
titeltext = font.render("Smash Bros", False, schwarz)

titel_rect = titeltext.get_rect()

#Text
title_text_x = width // 2 - titeltext.get_width() // 2
title_text_y = height // 8 - titeltext.get_height() // 2

titel_rect.topleft = (title_text_x, title_text_y)
#Text anzeigen lassen
screen.blit(titeltext, titel_rect)

pygame.display.flip()


#dass sich der Bildschirm schließen lässt
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.QUIT()