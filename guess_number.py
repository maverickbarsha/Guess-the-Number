import random
import winsound
def getHighScore():
    with open("high_scores.txt") as f:
        line = f.readline()
        li = line.split()
        return (li[0], li[1])

def setHighScore(name, score):
    with open("high_scores.txt", 'w+') as f:
        f.flush()
        toWrite = name +  " " + str(score)
        f.write(toWrite)

def main():
    usr = input("Enter your name: ").replace(" ", "").strip().split()
    username = "".join(usr)
    c = 0
    for x in range(1):
        p = (random.randint(1, 100))
    print("WELCOME TO GUESS THE NUMBER GAME")

    for i in range(10):
        w = int(input("\n Guess the number 1 to 100 : \n"))
        while (w <= 0 or w > 100):
            print("ERROR")
            w = int(input("\n Guess the number 1 to 100 : \n"))
        if p == w:
            print("congratulations", username + "!", "you are right!!")
            print("It took", c, "times to guess your number")
            score = int(100 / (c + 1))
            print("the score is ", score)
            highScoreName, highScore = getHighScore()
            if score > int(highScore):
                print("You have set new HighScore!")
                setHighScore(username, score)
            highScoreName, highScore = getHighScore()
            print("HIGH SCORE:  ",highScoreName, highScore)
        elif p > w:
            print("guess higher")
            c = c + 1
        else:
            print("guess lower")
            c = c + 1
    print("----------------EXIT-----------------------")
    winsound.MessageBeep()

    print("Your Score is 0")

    print("The correct number is", p)

if __name__ == '__main__':
    main()
