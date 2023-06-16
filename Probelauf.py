
import pygame

#Angaben zu den Bildschirmdimensionen
(width, height) = (600,600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smash Bros")
pygame.display.flip()

#Hintergrundbild
background_image = pygame.image.load("ai.jpg")
#Schriftart
font = pygame.font.Font(None, 64)
#Titeltext
title_text_surface = font.render("Smash Bros", False, (255, 0, 255))

#dass sich der Bildschirm schließen lässt
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
