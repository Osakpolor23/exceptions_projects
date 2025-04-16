# Exception Handling in Python: Practical Applications
This repository contains four Python programs that solve everyday problems with clean, structured logic, each designed to reinforce exception handling in real-world scenarios. Each script is interactive and validates user input while delivering clear results, ensuring robust and user-friendly experiences.

## Projects Overview

### **1. outdated.py**

**Description**
outdated.py converts a date entered in MM/DD/YYYY or Month DD, YYYY format into the internationally accepted YYYY-MM-DD format in accordance to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

**Features**
    Supports two common date formats.

    Standardizes the date into a consistent YYYY-MM-DD format.

    Handles invalid inputs gracefully.

**Sample Input:**

    Date: September 5, 2025

**Expected Output:**

    2025-09-05

**Sample Input:**

    Date: 10/15/2023

**Expected Output:**

    2023-10-15

### **2. grocery.py**

**Description**
grocery.py allows a user to create a grocery list, tracking how many times each item is entered. Items are sorted alphabetically and displayed in uppercase.

**Features**
    Users enter one item per line.

    Stops collecting items upon Ctrl+D (EOF).

    Outputs each item along with its occurrence count.

**Sample Input:**

    apple  
    banana  
    apple  
    orange  
    banana  
    orange  
    orange

**Expected Output:**

    2 APPLE  
    2 BANANA  
    3 ORANGE  

### **3. taqueria.py**

**Description**
taqueria.py allows users to place an order from Felipe’s Taqueria **[menu](https://www.felipesboston.com/menu)** in ***[Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square)*** and continuously updates the total cost after each item is entered until the user inputs **CTRL+D (or EOF)**

**Features**
    Handles case-insensitive input (e.g., "burrito" and "Burrito" are treated the same).

    Ignores invalid menu items.

    Displays the total cost formatted to two decimal places after each item is entered.

**Sample Input:**

    Item: burrito
    $7.50  
    Item: taco  
    $10.50  
    Item: super quesadilla  
    $20.00  
    Item: pizza  (Invalid item, ignored and reprompts)  
    Item: nachos  
    $31.00  

**Expected Output:**

    Total: $31.00

### **4. fuel.py**

**Description**
fuel.py takes a fraction (X/Y) input representing a fuel gauge and converts it to a percentage. If the percentage is very low or very high, it returns "E" (empty) or "F" (full).

**Features**
    Handles division and input errors gracefully.

    Converts fraction into a percentage.

    Returns "E" for 1% or less, "F" for 99% or more and the percentage value for others.

**Sample Input:**

    Fraction: 3/4

**Expected Output:**

    75%

**Sample Input:**

    Fraction: 1/100

**Expected Output:**

    E

**Sample Input:**

    Fraction: 99/100

**Expected Output:**

    F

Feel free to clone or fork this repository and contribute to these problem sets by adding more scenarios or enhancing the existing ones.