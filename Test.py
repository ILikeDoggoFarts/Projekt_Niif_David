import pygame

pygame.init()

#Angaben zu den Bildschirmdimensionen
width = 600
height = 600

screen_1 = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smash Bros")

weiss = [255, 255, 255]
schwarz = [0, 0, 0]
#Hintergrundbild
screen_1.fill(schwarz)
#Schriftart
font = pygame.font.Font(None, 60)

#Titeltext
titeltext = font.render("Smash Bros", True, weiss)
titel_rect = titeltext.get_rect()

#Text zentrieren
title_text_x = width // 2 - titeltext.get_width() // 2
title_text_y = height // 4 - titeltext.get_height() // 2

titel_rect.topleft = (title_text_x, title_text_y)

#Text anzeigen lassen
screen_1.blit(titeltext, titel_rect)

#press enter to ontinue
press_enter_text = font.render("Press enter to continue!", True, weiss)
press_enter_text_rect = press_enter_text.get_rect()

press_enter_text_x = width // 2 - press_enter_text.get_width() // 2
press_enter_text_y = height // 2 - press_enter_text.get_height() // 2

press_enter_text_rect.topleft = (press_enter_text_x, press_enter_text_y)

screen_1.blit(press_enter_text, press_enter_text_rect)


pygame.display.flip()


#dass sich der Bildschirm schließen lässt
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.QUIT()