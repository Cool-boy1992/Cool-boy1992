"""Guess  the correct number between 0 - 100 """
import random
Num1=random.randint(1, 100)
i=0
while i<10:
    i=i+1
    if(i==6):
        print("Number of attempt :", i)
        print("Number of guess left: ", (6 - i))
        print("GAME OVER,YOU HAVE CROSSED THE MAXIMUM LIMIT OF GUESSES")

        break
    num = int(input("Guess your number : "))
    if(num==Num1):
        print("Congratulations,you have guessed correct number")
        print("Number of attempt :", i)
        print("Number of guess left: ",(6-i))
        break
    elif (num<Num1):
        print("you have guessed a number smaller then the number")
        print("Number of attempt :", i)
        print("Number of guess left: ", (6 - i))
        continue
    elif(num>Num1):
        print("you have guessed a number greater then the number")
        print("Number of attempt :", i)
        print("Number of guess left: ", (6 - i))
        continue