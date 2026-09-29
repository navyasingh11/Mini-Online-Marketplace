from data import products


def search_by_name():

    print("\nSEARCH BY NAME")

    search_name = input("Enter product name: ").lower().strip()

    found = False

    for product_id, product in products.items():

        if search_name in product["name"].lower():

            print("\nProduct ID:", product_id)
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: ₹", product["price"])
            print("Quantity:", product["quantity"])
            print("Tags:", ", ".join(product["tags"]))

            found = True

    if not found:
        print("No products found.")


def view_by_category(allow_cart=False):

    while True:

        print("\nSELECT CATEGORY ")

        print("1. Electronics")
        print("2. Books")
        print("3. Furniture")
        print("4. Clothes")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            category = "Electronics"

        elif choice == "2":
            category = "Books"

        elif choice == "3":
            category = "Furniture"

        elif choice == "4":
            category = "Clothes"

        elif choice == "5":
            return True

        else:
            print("Choice not valid.")
            continue

        result = category_menu(category, allow_cart)

        if result:
            return True



def category_menu(category, allow_cart=False):

    while True:

        print("\n================================")
        print(category.upper())
        print("================================")

        print("1. View All Products")
        print("2. Filter by Tag")
        print("3. Filter by Price")
        print("4. Search by Name")

        if allow_cart:
            print("5. Add to Cart")
            print("6. Back to Main Menu")
        else:
            print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            view_category_products(category)

        elif choice == "2":

            filter_category_by_tag(category)

        elif choice == "3":

            filter_category_by_price(category)

        elif choice == "4":

            search_category_by_name(category)

        elif choice == "5" and allow_cart:

            from cart import add_to_cart

            add_to_cart()

        elif choice == "5" and not allow_cart:

            return True

        elif choice == "6" and allow_cart:

            return True

        else:

            print("Invalid choice.")



def view_category_products(category):

    print("\n==========", category.upper(), "PRODUCTS")

    found = False

    for product_id, product in products.items():

        if product["category"] == category:

            print("\nProduct ID:", product_id)
            print("Name:", product["name"])
            print("Price: ₹", product["price"])
            print("Quantity:", product["quantity"])
            print("Tags:", ", ".join(product["tags"]))

            found = True

    if not found:
        print("No products found.")


def filter_category_by_tag(category):

    print("\nFILTER BY TAG")

    tag = input("Enter tag: ").lower().strip()

    found = False

    for product_id, product in products.items():

        if product["category"] == category:

            if tag in product["tags"]:

                print("\nProduct ID:", product_id)
                print("Name:", product["name"])
                print("Price: ₹", product["price"])
                print("Quantity:", product["quantity"])
                print("Tags:", ", ".join(product["tags"]))

                found = True

    if not found:
        print("No products found with this tag in", category)



def filter_category_by_price(category):

    print("\n FILTER BY PRICE ")

    try:

        minimum = float(input("Enter minimum price: "))
        maximum = float(input("Enter maximum price: "))

    except ValueError:

        print("Please enter valid numbers.")
        return

    if minimum > maximum:

        print("Minimum price cannot be greater than maximum price.")
        return

    found = False

    for product_id, product in products.items():

        if product["category"] == category:

            if minimum <= product["price"] <= maximum:

                print("\nProduct ID:", product_id)
                print("Name:", product["name"])
                print("Price: ₹", product["price"])
                print("Quantity:", product["quantity"])
                print("Tags:", ", ".join(product["tags"]))

                found = True

    if not found:
        print("There are no products in this price range.")



def search_category_by_name(category):

    print("\nSEARCH BY NAME")

    name = input("Enter product name: ").lower().strip()

    found = False

    for product_id, product in products.items():

        if product["category"] == category:

            if name in product["name"].lower():

                print("\nProduct ID:", product_id)
                print("Name:", product["name"])
                print("Price: ₹", product["price"])
                print("Quantity:", product["quantity"])
                print("Tags:", ", ".join(product["tags"]))

                found = True

    if not found:
        print("No products found.")


def filter_by_price():

    print("\nFILTER BY PRICE ")

    try:

        minimum = float(input("Enter minimum price: "))
        maximum = float(input("Enter maximum price: "))

    except ValueError:

        print("Number not valid.")
        return

    if minimum > maximum:

        print("Minimum price cannot be greater than maximum price.")
        return

    found = False

    for product_id, product in products.items():

        if minimum <= product["price"] <= maximum:

            print("\nProduct ID:", product_id)
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: ₹", product["price"])
            print("Quantity:", product["quantity"])
            print("Tags:", ", ".join(product["tags"]))

            found = True

    if not found:
        print("There are no products in this price range.")


def filter_by_tag():

    print("\nFILTER BY TAG ")

    tag = input("Enter tag: ").lower().strip()

    found = False

    for product_id, product in products.items():

        if tag in product["tags"]:

            print("\nProduct ID:", product_id)
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: ₹", product["price"])
            print("Quantity:", product["quantity"])
            print("Tags:", ", ".join(product["tags"]))

            found = True

    if not found:
        print("No products found with this tag.")