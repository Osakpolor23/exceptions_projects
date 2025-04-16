# define the main function
def main():
    # assign the output of get_gauge function to fuel
    fuel = get_gauge()
    # print fuel
    print(fuel)


# define the get_gauge function
def get_gauge():
    # initiate an infinite loop
    while True:
        try:
            # prompt the user for input and remove whitespaces
            my_fuel = input("Fraction: ").strip()

            # split the input into the parts
            parts = my_fuel.split("/")

            # assign the component parts to x and y and convert to ints using map
            x, y = map(int, parts)

            # ensure x is lesser or equal to y and y is not zero
            if x <= y and y != 0:

                # Carry out the division, convert to a percentage and round to the nearest whole number
                percentage = round((x / y) * 100)

                # fulfil the various conditions and return the outputs
                if percentage <= 1:
                    return "E"  # E for Empty
                elif percentage >= 99:
                    return "F"  # F for Full
                else:
                    return f"{percentage}%" # return the percentage unchanged

            # otherwise, continue the loop
            else:
                continue

        # catch every ValueError and ZeroDivisionError i.e from int() and dividing numerator by zero
        except (ValueError, ZeroDivisionError):
            # silently ignore without outputing anything
            pass

# call the main function to execute the program
if __name__ == "__main__":
    main()
