from settings import *
from button import Button
import random

class MathGame:
    def __init__(self):
        self.gameMode = "home"
        self.inputText = ""

    def display(self):
        home.update()
        addSub.update()
        multi.update()
        div.update()


class Tab:
    def __init__(self):
        self.correct = 0
        self.questions = 0
        self.percent = 0
        self.digits = 3
        self.numberAmount = 2
        self.tabName = ""
        self.equationAnswer = ""
        self.bottomText = text3.render(f"Correct: {self.correct}     Questions: {self.questions}     Percent: {self.percent}%",True,white)
        self.bottomTextRect = self.bottomText.get_rect(center = (WIDTH//2,HEIGHT - 50))
        self.equationAnswer = None
        self.digitButton = Button(700,0,150,100,f"Digit:{self.digits}",25,gray)
        self.numberButton = Button(850, 0, 150, 100, f"Number:{self.numberAmount}", 25, gray)

    def update(self):
        if mathGame.gameMode == self.tabName:
            self.display()
            self.displayButton()

    def reset(self):
        self.createQuestion()

    def answer(self,answer):
        print((answer,self.equationAnswer))
        print((type(answer),type(self.equationAnswer)))

        if answer == self.equationAnswer:
            print("correct")
            correctSound.play()
            self.correct += 1
            self.questions += 1
            self.percent = round((self.correct/self.questions) * 100)
            # pygame.draw.rect(screen,green,(0,HEIGHT - 200,WIDTH,200))
        else:
            print("incorrect")
            incorrectSound.play()
            self.questions += 1
            self.percent = round((self.correct/self.questions) * 100)
            # pygame.draw.rect(screen, red, (0, HEIGHT - 200, WIDTH, 200))

        self.bottomText = text3.render(f"Correct: {self.correct}     Questions: {self.questions}     Percent: {self.percent}%",True,white)
        self.bottomTextRect = self.bottomText.get_rect(center = (WIDTH//2,HEIGHT - 50))
        self.reset()

    def displayResults(self):
        screen.blit(self.bottomText,self.bottomTextRect)

    def createQuestion(self):
        pass

    def display(self):
        print("2")

    def displayButton(self):
        self.digitButton.display()
        self.numberButton.display()

class Home(Tab):
    def __init__(self,tabName):
        super().__init__()
        self.textSurf = text1.render("Choose a Mode",True,"white")
        self.rect = self.textSurf.get_rect(center = (WIDTH // 2,400))
        self.tabName = tabName

    def update(self):
        if mathGame.gameMode == self.tabName:
            self.display()


    def display(self):
        screen.blit(self.textSurf,self.rect)

class addSub(Tab):
    def __init__(self,tabName):
        super().__init__()
        self.tabName = tabName
        self.createQuestion()
    def createQuestion(self):
        equation = ""
        for i in range(self.numberAmount):
            if i < self.numberAmount - 1:
                num = random.randint(1,10 ** self.digits)
                op = random.choice("+-")
                equation += f"{num} {op} "
            else:
                num = random.randint(1, 10 ** self.digits)
                equation += f"{num}"

        self.textSurf = text1.render(equation, True, "white")
        self.rect = self.textSurf.get_rect(center = (WIDTH // 2, 400))
        self.equationAnswer = eval(equation)

    def display(self):
        screen.blit(self.textSurf,self.rect)
        self.displayResults()


class Multiply(Tab):
    def __init__(self,tabName):
        super().__init__()
        self.tabName = tabName
        self.digits = 2
        self.numberAmount = 2

        self.equationAnswer = None
        self.createQuestion()
    def createQuestion(self):
        equation = ""
        for i in range(self.numberAmount):
            if i < self.numberAmount - 1:
                num = random.randint(1,10 ** self.digits)
                equation += f"{num} * "
            else:
                num = random.randint(1, 10 ** self.digits)
                equation += f"{num}"

        self.textSurf = text1.render(equation, True, "white")
        self.rect = self.textSurf.get_rect(center = (WIDTH // 2, 400))
        self.equationAnswer = eval(equation)

    def display(self):
        screen.blit(self.textSurf,self.rect)
        self.displayResults()

class Divide(Tab):
    def __init__(self,tabName):
        super().__init__()
        self.tabName = tabName
        self.digits = 2
        self.numberAmount = 2

        self.equationAnswer = None
        self.createQuestion()
    def createQuestion(self):
        equation = ""
        for i in range(self.numberAmount):
            if i < self.numberAmount - 1:
                num = random.randint(1,10 ** self.digits)
                equation += f"{num} / "
            else:
                num = random.randint(1, 10 ** self.digits)
                equation += f"{num}"

        self.textSurf = text1.render(equation, True, "white")
        self.rect = self.textSurf.get_rect(center = (WIDTH // 2, 400))
        self.equationAnswer = round(eval(equation),2)

    def display(self):
        screen.blit(self.textSurf,self.rect)
        self.displayResults()

home = Home("home")
addSub = addSub("+-")
multi = Multiply("*")
div = Divide("/")

mathGame = MathGame()