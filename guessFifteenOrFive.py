while True:
    number = int(input("Enter a number between 1 to 15: "))
    match number:
        case 5:
            print("You entered a 5, Game Over!!!")
            break
        case 15:
            print("You entered a 15, Game Over!!!")
            break
        case _:
            print("You entered", number)
            continue
