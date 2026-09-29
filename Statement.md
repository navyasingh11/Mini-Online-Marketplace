# 5.2 Project Statement

## 1. Problem Statement

Shopping platforms can become difficult to manage when product browsing, product management, shopping carts, and checkout are handled separately. This project aims to provide a simple online marketplace where these basic activities can be performed through one application.

The Mini Online Marketplace is designed as a command-line application that allows sellers to manage their products and buyers to browse products, search for items, add products to a cart, and place orders. The project provides a simple way to demonstrate the basic workflow of an online shopping system without the complexity of a web interface or database.

## 2. Scope of the Project

The scope of the project covers the basic operations required in a small online marketplace.

For sellers, the system allows them to:
 Add new products.
 View available products.
 View products by category.
 Update product information such as name, price, quantity, and tags.
 Delete products.

For buyers, the system allows them to:
 Browse products by category.
 View all available products.
 Search for products by name.
 Filter products by price and tags.
 Add products to a shopping cart.
 Remove or update items in the cart.
 View the cart total.
 Complete the checkout process.

The project focuses on the core shopping workflow. It does not include features such as user accounts, online payments, a database, delivery tracking, or a web/mobile interface. Product and cart information is maintained in memory while the application is running.

## 3. Target Users

The project is intended for two main types of users:

### Sellers

Sellers can use the system to manage the products available in the marketplace. They can add new products, update existing product details, view products, and remove products that are no longer available.

### Buyers

Buyers can use the system to find and purchase products. They can browse different categories, search and filter products, manage their shopping cart, and place an order through the checkout process.

The project can also be useful for students or beginners who want to understand how the basic components of an e-commerce application can work together.

## 4. High-Level Features

The major features of the Mini Online Marketplace are:

- Seller Management – Add, view, update, and delete products.
- Product Browsing – View products individually, by category, or as a complete catalog.
- Product Search – Search for products using their names.
- Product Filtering – Filter products using price ranges and tags.
- Shopping Cart – Add, remove, update, and view cart items.
- Stock Management – Check product availability and update stock after a successful purchase.
- Checkout – Calculate the subtotal, apply applicable discounts, and display the final amount.
- Order Confirmation – Allow the buyer to confirm or cancel an order.
- Command-Line Interface – Provide a simple menu-driven interface for interacting with the marketplace.
