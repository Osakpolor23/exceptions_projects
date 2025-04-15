# defined main function
def main():
    # assign the output of get_list function to grocery
    grocery = get_list()
    # print grocery
    print(grocery)


# define the get_list function
def get_list():
    # define an empty dictionary
    my_dict = {}

    while True:
        try:
            # prompt the user for input
            item = input().strip().lower()
            # check if item is in dictionary
            if item in my_dict:
                # increment the count
                my_dict[item] += 1
            # if the item doesn't exist, add it and map it to a value of 1
            else:
                my_dict[item] = 1

        # EOFError(End of File Error) when the user inputs ctrl + D should end the program
        except EOFError:
            break

    # create an empty list to store the formated items
    grocery_list = []

    # append the keys i.e items and their values(i.e counts) to the list
    for keys in sorted(my_dict.keys()):
        grocery_list.append(f"{my_dict[keys]} {keys.upper()}")

    # return the list as a single string but separated with each new line
    return "\n".join(grocery_list)

# call the main function to run the program
if __name__ == "__main__":
    main()
