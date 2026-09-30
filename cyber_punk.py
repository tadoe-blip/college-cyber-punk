door = input("Pick door 1, 2, or 3: ")

if door == "1":
    book = input("Pick book 1, 2, or 3: ")

    if book == "1":
        print("You feel dizzy and return to the first room.")
    elif book == "2":
        print("You find a secret passage and escape the room!")
    elif book == "3":
        print("Flames come out of the book. Game over.")
    else:
        print("Invalid choice.")

elif door == "2":
    bowl = input("Pick bowl 1, 2, or 3: ")

    if bowl == "1":
        print("You float away and do not know what happens.")
    elif bowl == "2":
        print("The floor opens and flames shoot out. Game over.")
    elif bowl == "3":
        print("You find a key and discover a secret passage!")
    else:
        print("Invalid choice.")

elif door == "3":
    print("The door opens and flames appear. Game over.")

else:
    print("Invalid choice.")

