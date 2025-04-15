# defined main function
def main():
    # assign the output of get_list function to grocery
    my_order = get_order()
    # print my_order
    print(my_order)


# define the get_order function
def get_order():
    my_dict = {"Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50,
    "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00 }

    # assign the total amount to be 0.00
    total = 0.00
    # create an infinite loop to keep asking for input until the user inputs ctrl + D(EOFError)
    while True:
        try:
            # prompt the use for item, remove whitespace and convert to title case
            item = input("Item: ").strip().title()

            # check if item is in dictionary
            if item in my_dict:
                # Add the item price(value) to total amount
                total += my_dict[item]

                # print the total amount
                print(f"Total: ${total:.2f}")

            # if the item doesn't exist, continue the loop
            else:
                continue

        # EOFError(End of File Error) when the user inputs ctrl + D should end the program
        except EOFError:
            break
    
    # return the total amount as a string with 2 decimal places
    return f"Total: ${total:.2f}"

# call the main function to run the program
if __name__ == "__main__":
    main()