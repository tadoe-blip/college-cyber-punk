
total_bill = 0.00

print("Welcome to ASIAN Tea House!")

while True:
    print("")
    print("ASIAN Tea House Menu")
    print("1. Burmese Milk Tea - $25.00")
    print("2. Thai Iced Tea - $25.00")
    print("3. Vietnamese Coffee - $25.00")
    print("4. Matcha - $25.00")
    print("5. Checkout")

    choice = input("Enter your choice: ")

    if choice == "1":
        total_bill = total_bill + 25
        print("You ordered Burmese Milk Tea.")

    elif choice == "2":
        total_bill = total_bill + 25
        print("You ordered Thai Iced Tea.")

    elif choice == "3":
        total_bill = total_bill + 25
        print("You ordered Vietnamese Coffee.")

    elif choice == "4":
        total_bill = total_bill + 25
        print("You ordered Matcha.")

    elif choice == "5":
        print("")
        print("Your total is", total_bill)

        print("")
        print("Choose a coupon:")
        print("1. SAVE10 - 10% off")
        print("2. STUDENT20 - 20% off")
        print("3. No coupon")

        coupon = input("Enter coupon option (1-3): ")

        if coupon == "1":
            discount = total_bill * 0.10
            total_bill = total_bill - discount
            print("10% discount applied!")

        elif coupon == "2":
            discount = total_bill * 0.20
            total_bill = total_bill - discount
            print("20% discount applied!")

        elif coupon == "3":
            print("No discount applied.")

        else:
            print("Invalid coupon option. No discount applied.")

        print("")
        print("ASIAN Tea House Receipt")
        print(f"Your final bill is ${total_bill:.2f}")
        print("Thank you for visiting ASIAN Tea House!")
        break

    else:
        print("Invalid choice. Please try again.")

    print(f"Current total is ${total_bill:.2f}")
