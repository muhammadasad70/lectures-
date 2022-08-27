print("hey and welcome to the number of guessing game")
print("in this game you have only 5 guess so be careful while playing")
x=3
no_of_guesser=1
while no_of_guesser<=5:
    guess_the_number=int(input("enter the number"))
    if guess_the_number<30:
        print("your guess is small")
    elif guess_the_number>30:
        print("sorry your guess is grater")
    else:
        print("hey congratulation you have won the game")
        break
    print("number of guesses left",5-no_of_guesser)
    no_of_guesser=no_of_guesser+1
if no_of_guesser>5:
    print("the game is over now")




