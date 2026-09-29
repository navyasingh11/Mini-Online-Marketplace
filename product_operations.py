from data import products


def add_product():

    print("\nADD PRODUCT")

    print("1. Electronics")
    print("2. Books")
    print("3. Furniture")
    print("4. Clothes")

    choice = input("Choose category number: ")

    if choice == "1":
        category = "Electronics"
        start_id = 100
        end_id = 199

    elif choice == "2":
        category = "Books"
        start_id = 200
        end_id = 299

    elif choice == "3":
        category = "Furniture"
        start_id = 300
        end_id = 399

    elif choice == "4":
        category = "Clothes"
        start_id = 400
        end_id = 499

    else:
        print("Category not valid.")
        return

    name = input("Enter product name: ")

    price = float(input("Enter price: "))

    quantity = int(input("Enter quantity: "))

    tag_input = input("Enter tags separated by commas: ")

    tags = set()

    for tag in tag_input.split(","):
        tags.add(tag.strip().lower())

    new_id = start_id

    while new_id in products:
        new_id += 1

    if new_id > end_id:
        print("No more product IDs available in this category.")
        return

    products[new_id] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "tags": tags
    }

    print("\nProduct added!")
    print("Product ID:", new_id)


def view_products():

    print("\nALL PRODUCTS")

    if len(products) == 0:
        print("No products available.")
        return

    for product_id, product in products.items():

        print("\nProduct ID:", product_id)
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: ₹", product["price"])
        print("Quantity:", product["quantity"])
        print("Tags:", ", ".join(product["tags"]))

        print("--------------------------------")


def view_product():

    print("\nVIEW PRODUCT")

    product_id = int(input("Enter product ID: "))

    if product_id not in products:
        print("Product not found.")
        return

    product = products[product_id]

    print("\nProduct ID:", product_id)
    print("Name:", product["name"])
    print("Category:", product["category"])
    print("Price: ₹", product["price"])
    print("Quantity:", product["quantity"])
    print("Tags:", ", ".join(product["tags"]))


def update_product():

    print("\nUPDATE PRODUCT")

    product_id = int(input("Enter product ID: "))

    if product_id not in products:
        print("Product not found.")
        return

    product = products[product_id]

    print("\nCurrent Product:")
    print("Name:", product["name"])
    print("Price: ₹", product["price"])
    print("Quantity:", product["quantity"])
    print("Tags:", ", ".join(product["tags"]))

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Price")
    print("3. Quantity")
    print("4. Tags")

    choice = input("Enter choice: ")

    if choice == "1":

        new_name = input("Enter new name: ")
        product["name"] = new_name

        print("Name updated.")

    elif choice == "2":

        new_price = float(input("Enter new price: "))
        product["price"] = new_price

        print("Price updated.")

    elif choice == "3":

        new_quantity = int(input("Enter new quantity: "))
        product["quantity"] = new_quantity

        print("Quantity updated.")

    elif choice == "4":

        tag_input = input("Enter new tags separated by commas: ")

        new_tags = set()

        for tag in tag_input.split(","):
            new_tags.add(tag.strip().lower())

        product["tags"] = new_tags

        print("Tags updated.")

    else:
        print("Invalid choice.")


def delete_product():

    print("\n DELETE PRODUCT ")

    product_id = int(input("Enter product ID: "))

    if product_id not in products:
        print("Product not found.")
        return

    print("Product:", products[product_id]["name"])

    confirmation = input(
        "Are you sure you want to delete this product? (y/n): "
    )

    if confirmation.lower() == "y":

        del products[product_id]

        print("Product deleted.")

    else:
        print("Delete cancelled.")