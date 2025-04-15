# define the main functuion to execute the program
def main():
    date = get_date()
    print(date)


# define get_date()
def get_date():
    valid_month = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December" ]
    while True:

        # prompt the user for date and remove whitespaces
        date = input("Date: ").strip()
        try:

            # check if the format is MM/DD/YYYY
            if "/" in date:

                # split the date into the component parts
                date_parts = date.split("/")

                # check if it has three parts
                if len(date_parts) == 3:

                    # map the parts to month, day and year
                    month, day, year = date_parts

                    # check if the parts are numerical i.e digits
                    if month.isdigit() and day.isdigit() and year.isdigit():

                        # convert all the parts to integers
                        month, day, year = int(month), int(day), int(year)

                        # ensure that month is between 1 and 12 and day is between 1 and 31
                        if 1 <= month <= 12 and 1 <= day <= 31:

                            # return the modified date in YYYY-MM-DD format
                            return f"{year:04d}-{month:02d}-{day:02d}"

            # otherwise check if the format is Month DD, YYYY
            elif "," in date:

                # split the date into its component parts
                date_parts = date.split(" ")

                # check if it has three parts and the 2nd and 3rd components are digits using their index positions
                if len(date_parts) == 3 and date_parts[1].replace(",", "").isdigit() and date_parts[2].isdigit():

                    # map the date parts to month_name, day and year -- remove the "," before storing day
                    month_name, day, year = date_parts[0].title(), date_parts[1].replace(",", ""), date_parts[2]

                    # check if the month_name is valid
                    if month_name in valid_month:

                        # Get the equivalent numerical value(i.e position) of each month in the list

                        month = valid_month.index(month_name) + 1  # 1 is added to tally with the calendar numbers

                        # change day and year to integers as well
                        day, year = int(day), int(year)

                        # validate that day is between 1 and 31
                        if 1 <= day <= 31:
                            
                            # return the modified date in YYYY-MM-DD format
                            return f"{year:04d}-{month:02d}-{day:02d}"

        # when there is a ValueError, do nothing and go over the loop again
        except ValueError:
            pass

# call the main function to execute the program
if __name__ == "__main__":
    main()



