#importing required module
import random

#function that takes in range and produces the correct number
def initialization():
    print("\n\tNUMBER GUESSING GAME \n\t--------------------")
    print("\n You get 7 turns!")
    flag=False
    while flag==False:
        rangeNum=input("Enter the range of numbers you want to guess from:  ")
        if rangeNum.isdigit():
            rangeNum=int(rangeNum)
            if rangeNum>0:
                flag=True
            else:
               print("\n\tWrong Input! Try again!")  
        else:
            print("\n\tWrong Input! Try again!")

    print("\n\tGUESS THE NUMBER!")

    correctAnswer=random.randrange(1,rangeNum+1)

    #returns the range and answer to the global scope
    return correctAnswer




def main():
    flag=True
    #Game continues as long as the player wants it 
    while flag==True:
        Answer=initialization()

        #guess counter
        guessedCorrectly=False
        numberOfGuesses=1


        while guessedCorrectly==False and numberOfGuesses<=7:
            guess=int(input("\nYour Guess: "))
            numberOfGuesses+=1
            #game logic
            if guess<Answer:
                print("\nGO HIGHER!")
            elif guess>Answer:
                print("\nGO LOWER!")
            else: 
                print("\n\tCONGATULATIONS YOU GUESSED THE NUMBER! Have a cookie!")
                guessedCorrectly=True
    
        #post game logic: game continuation? and end screen
        if guessedCorrectly==True:
            print("\n\tYou took",numberOfGuesses-1,"tries to guess it correctly")
        else:
            print("\n\tTHE CORRECT ANSWER WAS {0}".format(Answer))
            print("\n\tSORRY! You lose, please try again.")
    
        validAnswer=False
        while validAnswer==False:
            choice=input("Would you like another go? [y/n]: ")
            if choice=="y":
                validAnswer=True
                print("\n\tHere we go again!")
            elif choice=="n":
                validAnswer=True
                flag=False
                print("\n\tGoodbye!")
            else:
                print("ERROR! You should answer either y or n")


main()