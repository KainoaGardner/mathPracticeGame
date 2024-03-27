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
        money.update()
        memory.update()
        puzzle.update()


class Tab:
    def __init__(self):
        self.font = text1
        self.fontSmaller = text3
        self.correct = 0
        self.questions = 0
        self.percent = 0
        self.digits = 3
        self.maxDigit = 5
        self.numberAmount = 2
        self.maxNumberAmount = 5
        self.tabName = ""
        self.equationAnswer = ""
        self.bottomText = self.fontSmaller.render(f"Correct: {self.correct}     Questions: {self.questions}     Percent: {self.percent}%",True,white)
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
        else:
            print("incorrect")
            incorrectSound.play()
            self.questions += 1
            self.percent = round((self.correct/self.questions) * 100)


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

class Money(Tab):
    def __init__(self,tabName):
        super().__init__()
        self.tabName = tabName
        self.digits = 2
        self.numberAmount = 2
        self.digitButton = None
        self.numberButton = None

        self.equationAnswer = None
        self.createQuestion()

    def createQuestion(self):
        equation = ""

        firstNumber = random.randint(1,10 ** (self.digits + 2)) / 100
        secondNumber = random.randint(int(firstNumber),int(firstNumber) + 1 + random.choice([1,5,10,20]))
        equation += f"{secondNumber} - {firstNumber}"
        equationDollar = f"${secondNumber} - ${firstNumber}"

        self.textSurf = text1.render(equationDollar, True, "white")
        self.rect = self.textSurf.get_rect(center = (WIDTH // 2, 400))
        self.equationAnswer = round(eval(equation),2)

    def displayButton(self):
        pass

    def display(self):
        screen.blit(self.textSurf,self.rect)
        self.displayResults()

class Memory(Tab):
    def __init__(self, tabName):
        super().__init__()
        self.tabName = tabName
        self.digits = 2
        self.numberAmount = 2
        self.maxNumberAmount = 10
        self.speed = 1

        self.speedButton = Button(700,0,100,100,f"Speed: {self.speed}",15,gray)
        self.digitButton = Button(900,0,100,100,f"Digit:{self.digits}",15,gray)
        self.numberButton = Button(800, 0, 100, 100, f"Number:{self.numberAmount}", 15, gray)

        self.enterSum = text1.render("Enter Sum", True, "white")
        self.enterSumRect = self.enterSum.get_rect(center=(WIDTH // 2, 400))

        self.counter = 0
        self.numberList = []

        self.equationAnswer = None
        self.createQuestion()

    def createQuestion(self):
        for i in range(self.numberAmount):
            num = random.randint(1, 10 ** self.digits)
            self.numberList.append(num)

        self.getSum()
        print(self.numberList)

    def reset(self):
        self.counter = 0
        self.numberList = []
        self.createQuestion()

    def getSum(self):
        self.equationAnswer = 0
        for num in self.numberList:
            self.equationAnswer += num

    def displayButton(self):
        self.digitButton.display()
        self.numberButton.display()
        self.speedButton.display()

    def display(self):
        self.counter += 1 * self.speed
        if self.counter // (FPS * 3) < len(self.numberList):
            self.textSurf = text1.render(str(self.numberList[self.counter // (FPS * 3)]), True, "white")
            self.rect = self.textSurf.get_rect(center=(WIDTH // 2, 400))
            self.indexText = text3.render(str((self.counter // (FPS * 3)) + 1), True, "white")
            self.indexRect = self.indexText.get_rect(center=(WIDTH // 2, 350))
            screen.blit(self.textSurf,self.rect)
            screen.blit(self.indexText,self.indexRect)
        else:
            screen.blit(self.enterSum,self.enterSumRect)
        self.displayResults()

class Puzzle(Tab):
    def __init__(self,tabName):
        super().__init__()
        self.tabName = tabName
        self.digits = 2
        self.numberAmount = 2
        self.maxNumberAmount = 4
        # self.maxDigit = 4
        self.equationAnswer = ""
        self.createQuestion()

    def createQuestion(self):
        equation = ""
        operatorEquation = ""

        for i in range(self.numberAmount):
            if i < self.numberAmount - 1:
                num = random.randint(1, 10 ** self.digits)
                oper = random.choice(["+","-","*","/"])
                equation += f"{num} ? "
                operatorEquation += f"{num} {oper} "
                self.equationAnswer += oper
            else:
                num = random.randint(1, 10 ** self.digits)
                equation += f"{num} "
                operatorEquation += f"{num}"



        equation += f"= {round(eval(operatorEquation), 2)}"

        self.textSurf = text1.render(equation, True, "white")
        self.rect = self.textSurf.get_rect(center=(WIDTH // 2, 400))

    def reset(self):
        self.equationAnswer = ""
        self.createQuestion()


    def display(self):
        screen.blit(self.textSurf,self.rect)
        self.displayResults()

home = Home("home")
addSub = addSub("+-")
multi = Multiply("*")
div = Divide("/")
money = Money("$")
memory = Memory("memory")
puzzle = Puzzle("puzzle")

mathGame = MathGame()