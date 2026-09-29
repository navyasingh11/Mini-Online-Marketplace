from data import products, cart

def calculate_total():

    total = 0

    for product_id, quantity in cart.items():

        product = products[product_id]

        total = total + (product["price"] * quantity)

    return total

def calculate_discount(total):

    if total >= 3000:

        return 300

    elif total >= 2000:

        return 200

    else:

        return 0


def checkout():

    print("\nCHECKOUT")

    if len(cart) == 0:

        print("No products in your cart.")
        return

    subtotal = calculate_total()

    discount = calculate_discount(subtotal)

    final_amount = subtotal - discount

    print("\nBILL")

    for product_id, quantity in cart.items():

        product = products[product_id]

        item_total = product["price"] * quantity

        print(
            product["name"],
            "x",
            quantity,
            " = ₹",
            item_total
        )

    print("Subtotal: ₹", subtotal)
    print("Discount: ₹", discount)
    print("Final Amount: ₹", final_amount)

    confirmation = input("Confirm order? (y/n): ")

    if confirmation.lower() == "y":


        for product_id, quantity in cart.items():

            products[product_id]["quantity"] -= quantity

        cart.clear()

        print("\nOrder placed successfully!")
        print("Thank you for shopping with us.")

    else:

        print("\nOrder cancelled.")