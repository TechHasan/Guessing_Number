n=15
no_of_guesses=1
print("Number of guess limit is 9\n")
while(no_of_guesses<=9):
    ab=int(input("Enter a value to guess:\n"))
    if ab<15:
        print("You just entered the less number please enter greater number to guess\n")
    elif ab>15:
        print("You just entered the greater number please enter the less number to guess\n")
    else:
        print("You won")
        print(no_of_guesses,"Number of guesses took to finish")
        break

    print(9-no_of_guesses, "number of guesses left")
    no_of_guesses=no_of_guesses+1
if(no_of_guesses>9):
    print("Game Over")
