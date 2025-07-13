import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame  # Import the pygame library

pygame.init()  # Initialize all imported pygame modules

# Set up the display window
screen = pygame.display.set_mode((400, 300))  # Window size: 400x300 pixels
pygame.display.set_caption("Pygame Button")  # Set window title

# Define button properties
button_color = (0, 200, 0)  # Button color (normal)
button_hover = (0, 255, 0)  # Button color when hovered
button_rect = pygame.Rect(150, 120, 100, 50)  # Button rectangle: x, y, width, height

# Set up font and render the button text
font = pygame.font.SysFont(None, 36)  # Font: default, size 36
button_text = font.render("Click me!", True, (255, 255, 255))  # White text

running = True  # Game loop flag
while running:
    # Get current mouse position and mouse button state
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop and close the game

        # Check for mouse button press
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the mouse click is inside the button rectangle
            if button_rect.collidepoint(event.pos):
                print("Button was clicked!")  # Action for button click

    screen.fill((30, 30, 30))  # Fill the screen with dark gray

    # Change button color if the mouse is hovering over it
    if button_rect.collidepoint(mouse_pos):
        color = button_hover
    else:
        color = button_color

    # Draw the button rectangle
    pygame.draw.rect(screen, color, button_rect)

    # Center the text on the button
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)  # Draw the text

    pygame.display.flip()  # Update the display

pygame.quit()  # Quit pygame modules
