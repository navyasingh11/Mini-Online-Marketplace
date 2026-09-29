from product_operations import view_products, view_product

from search import (
    search_by_name,
    view_by_category,
    filter_by_price,
    filter_by_tag
)

from cart import (
    add_to_cart,
    remove_from_cart,
    update_cart,
    view_cart
)

from checkout import checkout

def buyer_menu():

    while True:

        print("\n")
        print("BUYER MENU")

        print("1. View by Category")
        print("2. View All Products")
        print("3. Search by Name")
        print("4. Filter by Price")
        print("5. Filter by Tag")
        print("6. Add to Cart")
        print("7. Remove from Cart")
        print("8. Update Cart")
        print("9. View Cart")
        print("10. Checkout")
        print("11. Back to Main Menu")

        choice = input("\nSelect your choice: ")

        if choice == "1":
         view_by_category(allow_cart=True)
        
        elif choice == "2":
            view_products()

        elif choice == "3":
            search_by_name()

        elif choice == "4":
            filter_by_price()

        elif choice == "5":
            filter_by_tag()

        elif choice == "6":
            add_to_cart()

        elif choice == "7":
            remove_from_cart()

        elif choice == "8":
            update_cart()

        elif choice == "9":
            view_cart()

        elif choice == "10":
            checkout()

        elif choice == "11":
            print("Returning to main menu...")
            break
        else:
            print("Choice not valid. Please try again.")