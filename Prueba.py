import collections

#Constants
PRODUCT_FIELDS = ["title", "author", "category", "price", "quantity_in_stock"]
SALE_FIELDS = ["client", "product_title", "quantity", "date", "discount"]

#  Data Structures
# Products stored as a dictionary where keys are product titles (for easy lookup)
# and values are dictionaries containing product details.
products = {}

# Sales stored as a list of dictionaries, each representing a sale.
sales = []

# Helper Functions

def validate_input(prompt, type_func, validation_func=None, error_message="Invalid input."):
    # Validates user input based on type and an optional custom validation function.
    while True:
        try:
            user_input = input(prompt)
            value = type_func(user_input)
            if validation_func and not validation_func(value):
                print(error_message)
            elif len(user_input) == 0:
                print(error_message)
            else:
                return value
        except ValueError:
            print(error_message)

def get_product_by_title(title):
    # Retrieves a product by its title.
    return products.get(title)

def calculate_net_income(total_gross_income, total_discount):
    # Calculates net income using a lambda function.
    return (lambda gross, discount: gross - discount)(total_gross_income, total_discount)

#Core Functionalities

## Inventory Management

def register_product():
    # Registers a new product in the inventory.
    print("\n--- Register New Product ---")
    title = validate_input("Enter product title: ", str).strip()
    if get_product_by_title(title):
        print(f"Error: Product with title '{title}' already exists.")
        return

    author = validate_input("Enter author name: ", str).strip()
    category = validate_input("Enter category: ", str).strip()
    price = validate_input("Enter price: ", float, lambda x: x > 0, "Price must be a positive number.")
    quantity = validate_input("Enter quantity in stock: ", int, lambda x: x >= 0, "Quantity must be a non-negative integer.")

    products[title] = {
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "quantity_in_stock": quantity
    }
    print(f"Product '{title}' registered successfully!")

def consult_product():
    # Consults and displays details of a product.
    print("\n--- Consult Product ---")
    title = validate_input("Enter product title to consult: ", str).strip()
    product = get_product_by_title(title)
    if product:
        print("\nProduct Details:")
        for key, value in product.items():
            print(f"- {key.replace('_', ' ').title()}: {value}")
    else:
        print(f"Product with title '{title}' not found.")

def update_product():
    # Updates details of an existing product.
    print("\n--- Update Product ---")
    title = validate_input("Enter product title to update: ", str).strip()
    product = get_product_by_title(title)
    if not product:
        print(f"Product with title '{title}' not found.")
        return

    print(f"Updating product: '{title}'. Leave blank to keep current value.")

    new_author = input(f"Enter new author (current: {product['author']}): ").strip()
    if new_author:
        product['author'] = new_author

    new_category = input(f"Enter new category (current: {product['category']}): ").strip()
    if new_category:
        product['category'] = new_category

    while True:
        new_price_str = input(f"Enter new price (current: {product['price']}): ").strip()
        if not new_price_str:
            break
        try:
            new_price = float(new_price_str)
            if new_price <= 0:
                print("Price must be a positive number.")
            else:
                product['price'] = new_price
                break
        except ValueError:
            print("Invalid price format.")

    while True:
        new_quantity_str = input(f"Enter new quantity in stock (current: {product['quantity_in_stock']}): ").strip()
        if not new_quantity_str:
            break
        try:
            new_quantity = int(new_quantity_str)
            if new_quantity < 0:
                print("Quantity must be a non-negative integer.")
            else:
                product['quantity_in_stock'] = new_quantity
                break
        except ValueError:
            print("Invalid quantity format.")

    print(f"Product '{title}' updated successfully!")

def delete_product():
    # Deletes a product from the inventory.
    print("\n--- Delete Product ---")
    title = validate_input("Enter product title to delete: ", str).strip()
    if title in products:
        del products[title]
        print(f"Product '{title}' deleted successfully!")
    else:
        print(f"Product with title '{title}' not found.")

## Sales Management

def register_sale():
    
    # Registers a new sale, validates stock, and updates inventory.
    
    print("\n--- Register New Sale ---")
    client_name = validate_input("Enter client name: ", str).strip()
    product_title = validate_input("Enter product title to sell: ", str).strip()
    
    product = get_product_by_title(product_title)
    if not product:
        print(f"Error: Product '{product_title}' not found.")
        return

    quantity_to_sell = validate_input(
        f"Enter quantity to sell (available: {product['quantity_in_stock']}): ",
        int,
        lambda x: x > 0,
        "Quantity must be a positive integer."
    )

    if quantity_to_sell > product['quantity_in_stock']:
        print(f"Error: Insufficient stock. Only {product['quantity_in_stock']} available.")
        return

    discount_percentage = validate_input(
        "Enter discount percentage (0-100, press Enter for 0): ",
        lambda x: float(x) if x else 0.0,
        lambda x: 0 <= x <= 100,
        "Discount must be between 0 and 100."
    )
    
    sale_date = input("Enter sale date (YYYY-MM-DD, press Enter for today): ").strip()
    if not sale_date:
        import datetime
        sale_date = datetime.date.today().strftime("%Y-%m-%d")

    # Update stock
    product['quantity_in_stock'] -= quantity_to_sell

    sale = {
        "client": client_name,
        "product_title": product_title,
        "quantity": quantity_to_sell,
        "date": sale_date,
        "unit_price": product['price'], # Store unit price at time of sale
        "discount_percentage": discount_percentage,
        "total_sale_price": (product['price'] * quantity_to_sell) * (1 - discount_percentage / 100)
    }
    sales.append(sale)
    print(f"Sale of {quantity_to_sell} units of '{product_title}' registered successfully!")

def consult_sales():
    # Displays all registered sales.
    print("\n--- Consult Sales ---")
    if not sales:
        print("No sales registered yet.")
        return

    for i, sale in enumerate(sales):
        print(f"\nSale #{i+1}:")
        for key, value in sale.items():
            print(f"- {key.replace('_', ' ').title()}: {value}")

## Reporting Module

def generate_top_selling_products_report():
    # Generates a report of the top 3 most sold products.
    print("\n--- Top 3 Most Sold Products Report ---")
    if not sales:
        print("No sales data available to generate report.")
        return

    product_sales_count = collections.defaultdict(int)
    for sale in sales:
        product_sales_count[sale['product_title']] += sale['quantity']

    sorted_products = sorted(product_sales_count.items(), key=lambda item: item[1], reverse=True)

    print("\nTop 3 Products:")
    if not sorted_products:
        print("No products sold yet.")
        return

    for i, (product_title, quantity_sold) in enumerate(sorted_products[:3]):
        print(f"{i+1}. {product_title} - {quantity_sold} units sold")

def generate_sales_by_author_report():
    # Generates a report of total sales grouped by author.
    print("\n--- Sales by Author Report ---")
    if not sales:
        print("No sales data available to generate report.")
        return

    author_sales = collections.defaultdict(float)
    for sale in sales:
        product = get_product_by_title(sale['product_title'])
        if product:
            author = product['author']
            author_sales[author] += sale['total_sale_price']
    
    if not author_sales:
        print("No sales recorded for any author yet.")
        return

    sorted_authors = sorted(author_sales.items(), key=lambda item: item[1], reverse=True)

    for author, total_revenue in sorted_authors:
        print(f"Author: {author} - Total Revenue: ${total_revenue:.2f}")

def calculate_income_report():
    # Calculates and displays net and gross income.
    print("\n--- Income Report ---")
    if not sales:
        print("No sales data available to calculate income.")
        return

    total_gross_income = sum(sale['unit_price'] * sale['quantity'] for sale in sales)
    total_discount_amount = sum(
        (sale['unit_price'] * sale['quantity']) * (sale['discount_percentage'] / 100)
        for sale in sales
    )
    
    net_income = calculate_net_income(total_gross_income, total_discount_amount)

    print(f"Total Gross Income (without discount): ${total_gross_income:.2f}")
    print(f"Total Discount Applied: ${total_discount_amount:.2f}")
    print(f"Total Net Income (with discount): ${net_income:.2f}")

def evaluate_inventory_performance():
    # Evaluates inventory performance based on sales.
    print("\n--- Inventory Performance Evaluation ---")
    if not sales and not products:
        print("No products or sales data available.")
        return

    # Products sold and their quantities
    product_sales_count = collections.defaultdict(int)
    for sale in sales:
        product_sales_count[sale['product_title']] += sale['quantity']

    # Performance metric: percentage of stock sold
    print("\nProduct Sales Performance (Percentage of Initial Stock Sold):")
    for title, product_data in products.items():
        initial_stock = product_data.get('initial_quantity', product_data['quantity_in_stock'] + product_sales_count.get(title, 0)) # Approximation if initial not stored
        sold_quantity = product_sales_count.get(title, 0)
        
        if initial_stock > 0:
            percentage_sold = (sold_quantity / initial_stock) * 100
            status = "High Demand" if percentage_sold >= 75 else ("Medium Demand" if percentage_sold >= 25 else "Low Demand")
            print(f"- {title}: {sold_quantity} sold out of {initial_stock} ( {percentage_sold:.2f}% ) - Status: {status}")
        else:
            print(f"- {title}: No initial stock recorded or stock was 0.")
    
    # Products with low stock
    print("\nProducts with Low Stock ( < 10 units):")
    low_stock_products = {title: data['quantity_in_stock'] for title, data in products.items() if data['quantity_in_stock'] < 10}
    if low_stock_products:
        for title, quantity in low_stock_products.items():
            print(f"- {title}: {quantity} units remaining")
    else:
        print("No products with low stock.")

# --- Menu and Main Program Flow ---

def pre_load_data():
    # Pre-loads initial product data into the system.
    global products
    products = {
        "Cien años de soledad": {
            "title": "Cien años de soledad",
            "author": "Gabriel Garcia Marquez",
            "category": "Fantasy",
            "price": 10.00,
            "quantity_in_stock": 50,
            "initial_quantity": 50 # For performance evaluation
        },
        "Habitos atomicos": {
            "title": "Habitos atomicos",
            "author": "James Clear",
            "category": "Self-help",
            "price": 12.50,
            "quantity_in_stock": 30,
            "initial_quantity": 30
        },
        "La ley de la atraccion": {
            "title": "La ley de la atraccion",
            "author": "Jerry Hicks, Esther Hicks",
            "category": "Self_help",
            "price": 18.75,
            "quantity_in_stock": 40,
            "initial_quantity": 40
        },
        "Piense y hagase rico": {
            "title": "Piense y hagase rico",
            "author": "Napoleon Hill",
            "category": "Self_help",
            "price": 15.00,
            "quantity_in_stock": 25,
            "initial_quantity": 25
        },
        "Padre rico padre pobre": {
            "title": "Padre rico padre pobre",
            "author": "Robert Kiyosaki, Sharon Lechter",
            "category": "No fiction",
            "price": 10.00,
            "quantity_in_stock": 35,
            "initial_quantity": 35
        }
    }
    print("Pre-loaded 5 products into the system.")

def display_menu():
    # Displays the main menu options to the user.
    print("\n" + "="*40)
    print("  Integral Inventory and Sales System")
    print("="*40)
    print("1. Inventory Management")
    print("2. Sales Management")
    print("3. Reports")
    print("4. Exit")
    print("="*40)

def display_inventory_menu():
    # Displays the inventory management menu.
    print("\n--- Inventory Management ---")
    print("1. Register Product")
    print("2. Consult Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Back to Main Menu")

def display_sales_menu():
    # Displays the sales management menu.
    print("\n--- Sales Management ---")
    print("1. Register Sale")
    print("2. Consult Sales")
    print("3. Back to Main Menu")

def display_reports_menu():
    # Displays the reports menu.
    print("\n--- Reports ---")
    print("1. Top 3 Most Sold Products")
    print("2. Sales Grouped by Author")
    print("3. Income Report (Net/Gross)")
    print("4. Inventory Performance Evaluation")
    print("5. Back to Main Menu")

def main():
    # Main function to run the inventory and sales management system.    
    pre_load_data()

    while True:
        display_menu()
        choice = validate_input("Enter your choice: ", str)

        if choice == '1':
            while True:
                display_inventory_menu()
                inv_choice = validate_input("Enter your choice: ", str)
                if inv_choice == '1':
                    register_product()
                elif inv_choice == '2':
                    consult_product()
                elif inv_choice == '3':
                    update_product()
                elif inv_choice == '4':
                    delete_product()
                elif inv_choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            while True:
                display_sales_menu()
                sale_choice = validate_input("Enter your choice: ", str)
                if sale_choice == '1':
                    register_sale()
                elif sale_choice == '2':
                    consult_sales()
                elif sale_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':
            while True:
                display_reports_menu()
                report_choice = validate_input("Enter your choice: ", str)
                if report_choice == '1':
                    generate_top_selling_products_report()
                elif report_choice == '2':
                    generate_sales_by_author_report()
                elif report_choice == '3':
                    calculate_income_report()
                elif report_choice == '4':
                    evaluate_inventory_performance()
                elif report_choice == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()