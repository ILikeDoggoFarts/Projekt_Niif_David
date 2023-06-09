# Projekt_Niif_David
Projekt von Niif und David. (Super cooles smash bros game)

use cases:

-	1:
-	Start the game by clicking on the icon
-	Exit the game

-	2:
- start the game by clicking on the icon
- press start
- choose your characters by clicking on one of them
- see countdown and get ready for playing
- play
- either loose or win
- see the end result after the game
- press return to menu
- play another game

-	3:
- start the game by clicking on the icon
- press start
- choose your characters by clicking on one of them
- see countdown and get ready for playing
- play
- either loose or win
- see the end result after the game
- press return to menu
- exit game

-	4:
- start the game by clicking on the icon
- press start
- choose your characters by clicking on one of them
- see countdown and get ready for playing
- play
- either loose or win
- see the end result after the game
- press on “play again”
- repeat


Reihenfolge Programieren:

First, you need to set up your development environment. Install Python, and install Pygame, a Python library for game development.

Create the Title screen: Create a Pygame window, display the game title, and draw two buttons for Start and Exit. Use Pygame's pygame.draw functions to draw rectangles for the buttons and text for their labels.

Implement button functionality: Check if the mouse is clicked on the buttons' rectangles, and change the screen accordingly. If the player clicks on the Exit button, exit the game. If the player clicks on the Start button, move to the character selection screen.

Character selection screen: Display a set of characters for the player to choose from. You can use images for the characters. Allow the player to select a character using the keyboard or mouse.

Map selection: Generate a list of maps and randomly select one for the game. You can use images for the maps.

Countdown: Before the game starts, display a countdown from 3 to 1. Use Pygame's pygame.time module to control the time.

Start the game: Once the countdown finishes, start the game. Display the two characters and the map. Use Pygame's pygame.sprite module to create the characters.

Player movements: Allow players to move their characters left, right, jump and attack using keyboard controls. Use Pygame's pygame.key module to capture keyboard events.

Collisions: Detect collisions between characters, maps, and attacks. Use Pygame's pygame.sprite.spritecollide method to detect collisions.

Life Bar: Display a life bar for each character. Update the life bar when a character is attacked.

End game screen: When a character's life bar gets empty, the game ends. Display a screen that tells which player has won. Add two buttons to the screen: Play Again and Return to Menu.

Implement button functionality: Check if the mouse is clicked on the buttons' rectangles, and change the screen accordingly. If the player clicks on Play Again, start a new game. If the player clicks on Return to Menu, go back to the Title screen.


character desription:
- all of them are able to punch, each one of them has a special way to attact.
 
 zap daddy:
  - can shoot bolts of lightning
 
 pyro puker:
  - is a basically a flame thrower
 
 fart quake:
 - can create a shockwave that pushes you away
      (be aware of the map border)
      
 Sneaky Pete the Ninja Beat:
 - can become invisible for up to 10 seconds every 30 seconds
 
 
 
 
  
