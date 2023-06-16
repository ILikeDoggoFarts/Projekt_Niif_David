import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fighting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game states
START_SCREEN = 0
CHARACTER_SELECTION = 1
GAMEPLAY = 2

# Variable to track current game state
current_state = START_SCREEN

# Character list
characters = ["Fighter A", "Fighter B", "Fighter C", "Fighter D"]
selected_character = None


# Start Screen
def start_screen():
    screen.fill(BLACK)

    # Draw title
    title_font = pygame.font.Font(None, 80)
    title_text = title_font.render("FIGHTING GAME", True, WHITE)
    title_text_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    screen.blit(title_text, title_text_rect)

    # Draw menu options
    menu_font = pygame.font.Font(None, 40)
    start_text = menu_font.render("1. Start Game", True, WHITE)
    start_text_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(start_text, start_text_rect)

    options_text = menu_font.render("2. Options", True, WHITE)
    options_text_rect = options_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(options_text, options_text_rect)

    quit_text = menu_font.render("3. Quit Game", True, WHITE)
    quit_text_rect = quit_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
    screen.blit(quit_text, quit_text_rect)

    pygame.display.update()


# Character Selection Screen
def character_selection():
    screen.fill(BLACK)

    # Draw title
    title_font = pygame.font.Font(None, 80)
    title_text = title_font.render("SELECT YOUR FIGHTER", True, WHITE)
    title_text_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 200))
    screen.blit(title_text, title_text_rect)

    # Draw character options
    character_font = pygame.font.Font(None, 60)
    for i, character in enumerate(characters):
        character_text = character_font.render(f"{i + 1}. {character}", True, WHITE)
        character_text_rect = character_text.get_rect(center=(screen_width // 2, screen_height // 2 + (i * 100)))
        screen.blit(character_text, character_text_rect)

    pygame.display.update()


# Gameplay
def gameplay():
    screen.fill(BLACK)

    # Draw gameplay elements
    gameplay_font = pygame.font.Font(None, 80)
    gameplay_text = gameplay_font.render(f"GAMEPLAY - {selected_character}", True, WHITE)
    gameplay_text_rect = gameplay_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(gameplay_text, gameplay_text_rect)

    pygame.display.update()


# Game Loop
running = True
start_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if current_state == START_SCREEN: