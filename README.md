<<<<<<< HEAD
# Prueba-de-Desempeño
=======
# Integrated Inventory and Sales Management System with Dynamic Reports

This Python program is an effective tool designed for inventory and sales management with dynamic reports. It allows you to perform fundamental operations such as registering new books, consulting books, updating books, deleting books.

## Main features Inventory Management

* **Book registration**: Allows you to add new books to the system, capturing their title, author, category, price and quantity in stock.
* **Book Query**: Facilitates the search for a specific book by its title. When it is found, it shows all relevant data, including price, quantity and category.
* **Book update**: Offers the functionality to modify the author's name, price, quantity already registered in the system and its category, allowing to keep it updated.
* **Book deletion**: Allows to remove the complete record of a book from the system, using its title.

## Sales Management Features

* **Customer registration**: Allows to register the name of the customer, the title of the book to be given, the amount to be carried, the percentage to be applied and the date on which the sale was made.
* **Sales Query**: Allows you to display the information of the customer whose book was sold, including: Name, Title of the book, quantity, date, price, and percentage.

## Features Reports

* **Top 3 Most Sold Products**: The program allows you to view and analyze the sales details of the top 3 most sold books. 
* **Sales Grouped by Author**: Allows you to view the number of books sold by the same author. 
* **Income Report (Net/Gross)**: Allows you to view the gross revenue (without discount), total discounts applied and total revenue.
* **Inventory performance evaluation**: Shows the status of each book depending on the purchase demand. 

## How to run the program

1.  **Open a terminal or command line**: Navigate to the directory where you saved the file.
2.  **Run the program**: In the terminal, type the following command and press Enter:
 ````bash
 python3 prueba.py
 ````

## User Manual

* Once the program starts, you will be greeted with a menu of options. Simply enter the number corresponding to the action you wish to perform and press Enter.

The use of each option is detailed below:

### 1. Inventory Management

* Action**: Enter `1` and press Enter.
* **Process**:
    * The system will send you to another menu of options with a choice from 1 to 5 depending on what you are looking for.
    * Register Product`: The system will ask you to enter the title of the book, the name of the author, the category of the book, the price and the quantity in stock, and the book will be registered.
    * `2. Consult Product`: This option will ask you for the title of the book, showing you all the details of the book in console.
    * `3. Update Product`: This option will ask you for the title of the book you want to update, after that it will ask you to enter the new name of the author of the book, after that it will ask you for the new category, the price and finally the quantity in stock.
    * `4. Delete Product`: This option allows you to delete any book in the system with only the title.
    * `5. Back to main menu`: This option allows you to go back to the main menu of the system.
* **Result**:
    * To begin with if in the main menu you enter a number or character that is not from 1 to 4 it will give you an error, repeating the action that you enter a number from 1 to 4 until it is fulfilled.
    * If you already chose option 1 and went to the second menu, you have to choose an option from 1 to 5 otherwise you will get an error and the question will repeat until it is true.

### 2. Sales Management

**Action**: Enter `2` and press Enter.
* **Process**:
    * The system will send you to another menu of options with a choice from 1 to 3 depending on what you are looking for.
    * Register Sale`: This option allows you to register the name of the customer to whom the book was sold, registering his name, title of the book, amount to take, percentage to apply and the date of delivery of the book.
    * `2. Consult sales`: This option shows a list of the customers who have bought books, their quantity, date, price and percentage.
    * `3. Back to main menu`: This option allows you to go back to the main menu of the system.
* Result:
    * If you do not enter a character you will get an error and it will repeat the same question until it is true.

### 3. Reports

* **Action**: Enter `3` and press Enter.
* **Process**:
    * The system will send you to another menu of options with a choice from 1 to 5 depending on what you are looking for.
    * Top 3 Most Sold Products`: This option will allow you to see in the console the most sold books of the moment.
    * Sales Grouped by Author`: This option will allow you to see in the console which books have sold the most by author.
    * `3. Income Report (Net/Gross)`: This option will allow you to see the income (with discounts, without discount and the total of all).
    * `4. Inventory Performance Evaluation`: This option will allow you to see the status of each book according to its demand from bestseller to worstseller.
    * `5. Back to main menu`: This option allows you to return to the main menu of the system.

### 4. Exit

* **Action**: Enter `4` and press Enter.
* **Process**:
    * `4. Exit`: This option will allow you to terminate the program completely.
>>>>>>> 897e6db (NIVELATORIAPY)
