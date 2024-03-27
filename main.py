import pygame

from game import *
from button import *

def main():
    run = True
    input = ""
    inputSurface = pygame.surface.Surface((WIDTH,100))
    inputSurface.fill(gray)
    text = text1.render(input,True,white)
    textRect = text.get_rect(center = (WIDTH // 2,HEIGHT - 150))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(input) > 0:
                        if mathGame.gameMode == "+-":
                            addSub.answer(int(input))
                        elif mathGame.gameMode == "*":
                            multi.answer(int(input))
                        elif mathGame.gameMode == "/":
                            div.answer(float(input))
                        elif mathGame.gameMode == "$":
                            money.answer(float(input))
                        elif mathGame.gameMode == "memory":
                            memory.answer(float(input))
                        elif mathGame.gameMode == "puzzle":
                            puzzle.answer(input)
                        input = ""
                elif event.key == pygame.K_BACKSPACE:
                    input = input[:-1]

                else:
                    if len(input) < 10:
                        if event.unicode in ["1","2","3","4","5","6","7","8","9","0",".","-"] and mathGame.gameMode in ["+-","*","/","$","memory"]:
                            input += event.unicode
                        elif event.unicode in ["+","-","*","/"] and mathGame.gameMode == "puzzle":
                            input += event.unicode
                text = text1.render(input, True, white)
                textRect = text.get_rect(center=(WIDTH // 2, HEIGHT - 150))


            buttonClicks(event)

        display(inputSurface, input, text, textRect)


def display(inputSurface,input,text,textRect):
    screen.fill(darkGray)
    mathGame.display()
    if mathGame.gameMode != "home":
        screen.blit(inputSurface, (0, HEIGHT - 200))
    if len(input) > 0:
        screen.blit(text, textRect)
    for button in buttons:
        button.display()
    pygame.display.update()
    clock.tick(FPS)

def buttonClicks(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mos = pygame.mouse.get_pos()
        if mos[1] < 100:
            if homeButton.clicked(mos):
                for button in buttons:
                    button.pressed = False
                input = ""
                homeButton.pressed = True
                mathGame.gameMode = homeButton.gameType
            elif addButton.clicked(mos):
                for button in buttons:
                    button.pressed = False
                input = ""
                addButton.pressed = True
                mathGame.gameMode = addButton.gameType
                addSub.reset()
            elif multiplyButton.clicked(mos):
                for button in buttons:
                    button.pressed = False
                input = ""
                multiplyButton.pressed = True
                mathGame.gameMode = multiplyButton.gameType
                multi.reset()
            elif divideButton.clicked(mos):
                for button in buttons:
                    button.pressed = False
                input = ""
                divideButton.pressed = True
                mathGame.gameMode = divideButton.gameType
                div.reset()
            elif moneyButton.clicked(mos):
                for button in buttons:
                    button.pressed = False
                input = ""
                moneyButton.pressed = True
                mathGame.gameMode = moneyButton.gameType
                money.reset()
            elif memoryButton.clicked(mos):
                for button in buttons:
                    button.pressed = False
                input = ""
                memoryButton.pressed = True
                mathGame.gameMode = memoryButton.gameType
                memory.reset()
            elif puzzleButton.clicked(mos):
                for button in buttons:
                    button.pressed = False
                input = ""
                puzzleButton.pressed = True
                mathGame.gameMode = puzzleButton.gameType
                puzzle.reset()


            for gameType in [addSub, multi, div, memory,puzzle]:
                if gameType.digitButton.clicked(mos):
                    if event.button == 1:
                        if gameType.digits < gameType.maxDigit:
                            gameType.digits += 1
                    elif event.button == 3:
                        if gameType.digits > 1:
                            gameType.digits -= 1
                    gameType.digitButton.text = gameType.digitButton.font.render(f"Digit:{gameType.digits}", True, white)
                    gameType.digitButton.textRect = gameType.digitButton.text.get_rect(center=(
                    gameType.digitButton.x + gameType.digitButton.width // 2,
                    gameType.digitButton.y + gameType.digitButton.height // 2))
                    gameType.reset()

                if gameType.numberButton.clicked(mos):
                    if event.button == 1:
                        if gameType.numberAmount < gameType.maxNumberAmount:
                            gameType.numberAmount += 1
                    elif event.button == 3:
                        if gameType.numberAmount > 2:
                            gameType.numberAmount -= 1
                    gameType.numberButton.text = gameType.numberButton.font.render(f"Number:{gameType.numberAmount}", True,
                                                                                   white)
                    gameType.numberButton.textRect = gameType.numberButton.text.get_rect(center=(
                    gameType.numberButton.x + gameType.numberButton.width // 2,
                    gameType.numberButton.y + gameType.numberButton.height // 2))
                    gameType.reset()

            if memory.speedButton.clicked(mos):
                if event.button == 1:
                    if memory.speed < 5:
                        memory.speed += 1
                elif event.button == 3:
                    if memory.speed > 1:
                        memory.speed -= 1
                memory.speedButton.text = memory.digitButton.font.render(f"Speed:{memory.speed}", True, white)
                memory.speedButton.textRect = memory.digitButton.text.get_rect(center=(
                memory.speedButton.x + memory.speedButton.width // 2,
                memory.speedButton.y + memory.speedButton.height // 2))
                memory.reset()

def setHighlight():
    pass

main()


