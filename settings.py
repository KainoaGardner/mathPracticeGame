import pygame

WIDTH = 1000
HEIGHT = 1000
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

pygame.init()
text1 = pygame.font.Font("font/LEMONMILK-Regular.otf",50)
text3 = pygame.font.Font("font/LEMONMILK-Regular.otf",35)

correctSound = pygame.mixer.Sound("audio/oOa3Pqxy.wav")
incorrectSound = pygame.mixer.Sound("audio/YM0HJmuy.wav")
correctSound.set_volume(.5)
incorrectSound.set_volume(.5)




white = "#ecf0f1"
gray = "#575757"
# gray = "#7f8c8d"
darkGray = "#282828"
lightGray = "#bdc3c7"
red = "#e74c3c"
green = "#2ecc71"

