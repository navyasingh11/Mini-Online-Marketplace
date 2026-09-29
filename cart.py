from data import products, cart

def add_to_cart():

    print("\nADD TO CART")

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Please enter a valid product ID.")
        return

    if product_id not in products:
        print("Product not found.")
        return

    product = products[product_id]

    if product["quantity"] == 0:
        print("Sorry, this product is not availabe in stock.")
        return

    print("Product:", product["name"])
    print("Available quantity:", product["quantity"])

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid quantity.")
        return

    if quantity <= 0:
        print("Quantity cannot be zero.")
        return

    current_quantity = cart.get(product_id, 0)

    if current_quantity + quantity > product["quantity"]:
        print("Quantity not available.")
        print("Available quantity:", product["quantity"] - current_quantity)
        return

    cart[product_id] = current_quantity + quantity

    print("Added to cart.")

def remove_from_cart():

    print("\nREMOVE FROM CART")

    if len(cart) == 0:
        print("No product in your cart.")
        return

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Please enter a valid product ID.")
        return

    if product_id not in cart:
        print("Product is not in cart.")
        return

    del cart[product_id]

    print("Product removed from cart.")


def update_cart():

    print("\nUPDATE CART")

    if len(cart) == 0:
        print("No product in your cart.")
        return

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Please enter a valid product ID.")
        return

    if product_id not in cart:
        print("Product is not in cart.")
        return

    product = products[product_id]

    print("Product:", product["name"])
    print("Available quantity:", product["quantity"])

    try:
        new_quantity = int(input("Enter new quantity: "))
    except ValueError:
        print("Please enter a valid quantity.")
        return

    if new_quantity <= 0:
        print("Quantity cannot be zero.")
        return

    if new_quantity > product["quantity"]:
        print("Not enough stock available.")
        return

    cart[product_id] = new_quantity

    print("Cart updated successfully.")


def view_cart():

    print("\nYOUR CART")

    if len(cart) == 0:
        print("No products in your cart.")
        return

    total = 0

    for product_id, quantity in cart.items():

        product = products[product_id]

        item_total = product["price"] * quantity

        print("\nProduct ID:", product_id)
        print("Name:", product["name"])
        print("Price: ₹", product["price"])
        print("Quantity:", quantity)
        print("Item Total: ₹", item_total)

        total = total + item_total

    print("\n")
    print("Cart Total: ₹", total)