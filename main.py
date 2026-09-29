from seller import seller_menu
from buyer import buyer_menu

def main():

    while True:

        print("\n")
        print("ONLINE MARKETPLACE")

        print("1. Seller")
        print("2. Buyer")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            seller_menu()

        elif choice == "2":
            buyer_menu()

        elif choice == "3":
            print("\nThank you for shopping with us!")
            break

        else:
            print("Choice is not valid. Please choose again.")

main()