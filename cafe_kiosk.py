
total_bill = 0

print("Welcome to ASIAN Tea House!")

while True:
    print("")
    print("ASIAN Tea House Menu")
    print("1. Burmese Milk Tea - $25")
    print("2. Thai Iced Tea - $25")
    print("3. Vietnamese Coffee - $25")
    print("4. Matcha - $25")
    print("5. Checkout")

    choice = input("Choose a number: ")

    if choice == "1":
        total_bill = total_bill + 25
        print("Burmese Milk Tea added")

    elif choice == "2":
        total_bill = total_bill + 25
        print("Thai Iced Tea added")

    elif choice == "3":
        total_bill = total_bill + 25
        print("Vietnamese Coffee added")

    elif choice == "4":
        total_bill = total_bill + 25
        print("Matcha added")

    elif choice == "5":
        print("Your total is $", total_bill)

        promo = input("Enter promo code or type no: ")

        if promo == "stu":
            if total_bill >= 5:
                total_bill = total_bill - 5
                print("Student discount $5 applied")

        else:
            print("No discount")

        print("Your final total is $", total_bill)
        print("Thank you for visiting ASIAN Tea House!")
        break

    else:
        print("Invalid choice")

    print("Current total is $", total_bill)
