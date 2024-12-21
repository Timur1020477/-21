weapon = False

def strangeCreature(name):
    actions = ["с", "у"]  # с - сражаться, у - убежать
    global weapon
    print(f"Появилось странное существо, похожее на гуля. {name}, вы можете либо сражаться, либо убежать. Что вы хотите сделать? (с/у)")
    userInput = ""
    while userInput not in actions:
        userInput = input()
        if userInput == "с":
            if weapon:
                print(f"{name}, вы убили гуля ножом, который нашли ранее. После того как вы двинулись вперед, вы нашли один из выходов. Поздравляем!")
            else:
                print(f"{name}, гуль убивает вас.")
            quit()
        elif userInput == "у":
            showSkeletons(name)
        else:
            print("Пожалуйста, выберите правильный вариант.")

def showSkeletons(name):
    directions = ["н", "в"]  # н - назад, в - вперед
    global weapon
    print(f"{name}, вы видите стену скелетов, когда заходите в комнату. Кто-то наблюдает за вами. Куда бы вы хотели пойти? (н/в)")
    userInput = ""
    while userInput not in directions:
        userInput = input()
        if userInput == "н":
            introScene(name)
        elif userInput == "в":
            strangeCreature(name)
        else:
            print("Пожалуйста, выберите правильный вариант.")

def hauntedRoom(name):
    directions = ["п", "л", "н"]  # п - вправо, л - влево, н - назад
    print(f"{name}, вы слышите странные голоса. Похоже, вы разбудили некоторых мертвецов. Куда бы вы хотели пойти? (п/л/н)")
    userInput = ""
    while userInput not in directions:
        userInput = input()
        if userInput == "п":
            print(f"{name}, несколько существ, похожих на гулей, начинают появляться, когда вы заходите в комнату. Вас убивают.")
            quit()
        elif userInput == "л":
            print(f"{name}, вы выбрались! Вы нашли выход.")
            quit()
        elif userInput == "н":
            introScene(name)
        else:
            print("Пожалуйста, выберите правильный вариант.")

def cameraScene(name):
    directions = ["в", "н"]  # в - вперед, н - назад
    print(f"{name}, вы видите камеру, которая была уронена на землю. Кто-то недавно был здесь. Куда бы вы хотели пойти? (в/н)")
    userInput = ""
    while userInput not in directions:
        userInput = input()
        if userInput == "в":
            print(f"{name}, вы выбрались! Вы нашли выход.")
            quit()
        elif userInput == "н":
            showShadowFigure(name)
        else:
            print("Пожалуйста, выберите правильный вариант.")

def showShadowFigure(name):
    directions = ["п", "н"]  # п - вправо, н - назад
    print(f"{name}, вы видите темную, туманную фигуру вдали. Вам становится страшно. Куда бы вы хотели пойти? (п/н)")
    userInput = ""
    while userInput not in directions:
        userInput = input()
        if userInput == "п":
            cameraScene(name)
        elif userInput == "н":
            introScene(name)
        else:
            print("Пожалуйста, выберите правильный вариант.")

def introScene(name):
    directions = ["л", "п", "в"]  # л - влево, п - вправо, в - вперед
    print(f"{name}, вы стоите на развилке, и вам нужно выбрать, в какой коридор пойти. Куда бы вы хотели пойти? (л/п/в)")
    userInput = ""
    while userInput not in directions:
        userInput = input()
        if userInput == "л":
            showShadowFigure(name)
        elif userInput == "п":
            showSkeletons(name)
        elif userInput == "в":
            hauntedRoom(name)
        else:
            print("Пожалуйста, выберите правильный вариант.")

if __name__ == "__main__":
    while True:
        print("Добро пожаловать в приключенческую игру!")
        print("Как заядлый путешественник, вы решили посетить катакомбы Парижа.")
        print("Однако во время исследования вы потерялись.")
        print("Вы можете выбрать, в каком направлении двигаться, чтобы найти выход.")
        print("игра была переведена умным тюленем! ")
        print("Давайте начнем с вашего имени: ")
        name = input()
        print(f"Удачи, {name}.")
        introScene(name)
