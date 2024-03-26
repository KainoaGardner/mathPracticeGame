from settings import *


class Button:
    def __init__(self,x,y,width,height,text,textSize,color):
        self.font = pygame.font.Font("font/LEMONMILK-Regular.otf", textSize)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gameType = text
        self.text = self.font.render(text,True,white)
        self.textRect = self.text.get_rect(center = (self.x + self.width // 2,self.y + self.height //2))
        self.highLight = pygame.Surface((self.width,self.height))
        self.highLight = self.highLight.convert_alpha()
        self.highLight.fill((0,0,0,50))
        self.color = color
        self.pressed = False


    def display(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
        if self.pressed:
            screen.blit(self.highLight,(self.x,self.y))
        screen.blit(self.text,self.textRect)

    def clicked(self,pos):
        return self.x <= pos[0] < self.x + self.width and self.y <= pos[1] < self.y + self.height

homeButton = Button(0,0,100,100,"home",25,gray)
homeButton.pressed = True
addButton = Button(100,0,100,100,"+-",50,gray)
multiplyButton = Button(200,0,100,100,"*",50,gray)
divideButton = Button(300,0,100,100,"/",50,gray)
cashButton = Button(400,0,100,100,"$",50,gray)
rememberButton = Button(500,0,100,100,"memory",20,gray)
puzzleButton = Button(600,0,100,100,"puzzle",25,gray)



buttons = [homeButton,addButton,multiplyButton,divideButton,cashButton,rememberButton,puzzleButton]