from settings import *
from game import mathGame
from button import buttons
def display():
    screen.fill(lightGray)
    mathGame.display()
    for button in buttons:
        button.display()
    pygame.display.update()
    clock.tick(FPS)