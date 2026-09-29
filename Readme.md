# Mini Online Marketplace

## 1. Project Overview

Mini Online Marketplace is a command-line Python application that simulates a simple online shopping platform with separate Seller and Buyer workflows.

The application maintains a product catalog containing product details such as name, category, price, quantity, and tags. Sellers can manage products, while buyers can browse, search, filter, manage their shopping cart, and complete checkout.

The application starts from `main.py`, which provides the main menu for selecting either the Seller or Buyer workflow.

## 2. Features

## Seller Features

   View products by category.
   View all available products.
   View details of a specific product.
   Add new products.
   Update product name, price, quantity, or tags.
   Delete products with confirmation.
   Automatically generate the next available product ID within the selected category.

### Buyer Features

   View products by category.
   View all products.
   Search products by name.
   Filter products by price range.
   Filter products by tag.
   Add products to the shopping cart.
   Remove products from the cart.
   Update cart quantities.
   View cart contents and total amount.
   Checkout and place an order.

### Shopping Cart & Checkout

   Prevent adding products when they are out of stock.
   Validate requested quantities against available stock.
   Calculate the cart subtotal.
   Apply discounts based on the subtotal:
       ₹200 discount for orders of ₹2,000 or more.
       ₹300 discount for orders of ₹3,000 or more.
   Display a final bill before order confirmation.
   Reduce product stock after a successful order.
   Clear the cart after an order is placed.

## 3. Technologies / Tools Used

   Python 3
   Python Dictionaries -- used to store product information.
   Python Sets -- used for product tags.
   Python Functions -- used to separate application functionality into modules.
   Command-Line Interface (CLI) -- used for user interaction.
   No external libraries or third-party dependencies are required.

## 4. Project Structure

``` text
Mini Online Marketplace/
│
├── main.py
├── buyer.py
├── seller.py
├── product_operations.py
├── search.py
├── cart.py
├── checkout.py
├── data.py
└── README.md
```

### File Description

  -----------------------------------------------------------------------
  File                                Purpose
  ----------------------------------- -----------------------------------
  `main.py`                           Starts the application and provides the Seller/Buyer main menu.

  `seller.py`                         Provides the Seller menu and connects seller operations.

  `buyer.py`                          Provides the Buyer menu and connects shopping operations.

  `product_operations.py`             Handles adding, viewing, updating, and deleting products.

  `search.py`                         Handles product search, category  browsing, and price/tag filtering.

  `cart.py`                           Handles adding, removing, updating, and viewing cart items.

  `checkout.py`                       Calculates totals, discounts, and processes checkout.

  `data.py`                           Stores the product catalog and current shopping cart.
  -----------------------------------------------------------------------

## 5. Steps to Install & Run the Project

### Prerequisites

Make sure Python 3 is installed on your system.

Check the Python installation using:

``` bash
python --version
```

or:

``` bash
python3 --version
```

### Installation

1.  Download or clone the project.
2.  Open a terminal/command prompt.
3.  Navigate to the project directory.

No additional packages need to be installed because the project uses
Python's built-in functionality only.

### Run the Application

Run:

``` bash
python main.py
```

If your system uses `python3`, run:

``` bash
python3 main.py
```

The application will display:

``` text
       MINI ONLINE MARKETPLACE
1. Seller
2. Buyer
3. Exit
```

Select the required option and follow the command-line prompts.

## 6. Instructions for Testing

The project can be tested manually through the command-line menus.

### Test 1: Seller - View Products

1.  Run `main.py`.
2.  Select 1. Seller**.
3.  Select 2. View All Products**.
4.  Verify that product IDs, names, categories, prices, quantities, and
    tags are displayed.

### Test 2: Seller - Add Product

1.  Select Seller from the main menu.
2.  Select 4. Add Product.
3.  Select a category.
4.  Enter a product name, price, quantity, and comma-separated tags.
5.  Verify that the product is added and a product ID is displayed.
6.  Select View All Products to verify the new product.

### Test 3: Seller - Update Product

1.  Select Seller.
2.  Select 5. Update Product.
3.  Enter an existing product ID.
4.  Select the field to update.
5.  Enter the new value.
6.  Verify that the updated information is displayed.

### Test 4: Seller - Delete Product

1.  Select Seller.
2.  Select 6. Delete Product**.
3.  Enter an existing product ID.
4.  Enter `y` when asked for confirmation.
5.  Verify that the product is no longer displayed.

### Test 5: Buyer - Search and Filter

1.  Select Buyer.
2.  Test Search by Name with part of a product name.
3.  Test Filter by Price using a valid minimum and maximum price.
4.  Test Filter by Tag using an existing tag.
5.  Verify that only matching products are displayed.



## 7. Notes

Product and cart information is stored in memory using Python data structures.
Data is not persisted to a database or file, so changes made during execution are lost when the application exits.
The application is intended as a simple command-line marketplace implementation.
