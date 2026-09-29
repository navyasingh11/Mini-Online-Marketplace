from product_operations import (
    add_product,
    view_products,
    view_product,
    update_product,
    delete_product
)

from search import view_by_category

def seller_menu():

    while True:

        print("\n")
        print("SELLER MENU")
        
        print("1. View by Category")
        print("2. View All Products")
        print("3. View Product")
        print("4. Add Product")
        print("5. Update Product")
        print("6. Delete Product")
        print("7. Back to Main Menu")

        choice = input("\nSelect your choice: ")

        if choice == "1":
            view_by_category(allow_cart=False)

        elif choice == "2":
            view_products()

        elif choice == "3":
            view_product()

        elif choice == "4":
            add_product()

        elif choice == "5":
            update_product()

        elif choice == "6":
            delete_product()

        elif choice == "7":
            print("Returning to main menu...")
            break

        else:
            print("Choice not valid. Please try again.")