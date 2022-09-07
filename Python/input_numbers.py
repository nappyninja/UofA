def SaveNumber():
    while True:
        try:
            number = int(input("Please enter a number: "))
            savefile = open("numbers.txt", "a")
            savefile.write(str(number)+ '\n')
            savefile.close()
        except ValueError:
            print("That is not a number")
            continue
        else:
            break

while True:
    response = input("Do you want to enter a number? y/n"+ "\n")
    if response.lower().startswith("y"):
        SaveNumber()
    elif response.lower().startswith("n"):
        print("Fine, goodbye")
        exit()
    else:
        print("That is not a valid response, please try again")