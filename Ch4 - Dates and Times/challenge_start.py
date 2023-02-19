# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# count number of specific weekday in given month & year
def main():
    # instructions
    print()
    print("This program will calculate the number of weekdays in a given month and year.")
    print("Enter 'exit' at any time to quit. Enter 'help' for more information.")
    print()

    run_program = True
    while(run_program):

        weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        
        # get weekday selection
        weekday = None
        while(weekday == None):
            weekday = input("Which day of the week (0-6) do you want to count? ")
            if weekday.lower() == "exit":
                weekday = None
                break
            elif weekday.lower() == "help":
                print()
                for i, day in enumerate(weekdays):
                    print(i, "-", day)
                print()
                weekday = None
                continue
            try:
                weekday = int(weekday)
            except ValueError as e:
                print("Invalid entry. Please enter a number from 0-6.\n")
                weekday = None
        
        # quit if user exits
        if weekday == None:
            return

        # get month selection
        month = None
        while(month == None):
            month = input("Of which month (1-12)? ")
            if month.lower() == "exit":
                month = None
                break
            elif month.lower() == "help":
                print()
                print(" 1 - January")
                print(" 2 - February")
                print(" 3 - March")
                print(" 4 - April")
                print(" 5 - May")
                print(" 6 - June")
                print(" 7 - July")
                print(" 8 - August")
                print(" 9 - September")
                print("10 - October")
                print("11 - November")
                print("12 - December")
                print()
                month = None
                continue
            try:
                month = int(month)
            except ValueError as e:
                print("Invalid entry. Please enter a number from 1-12.\n")
                month = None
          
        # quit if user exits
        if month == None:
          return
        
        # get year selection
        year = None
        while(year == None):
            year = input("In what year (YYYY)? ")
            if year.lower() == "exit":
                year = None
                break
            try:
                year = int(year)
            except ValueError as e:
                print("Invalid entry. Please enter a valid year.\n")
                year = None

        # quit if user exits
        if year == None:
            return
        
        cal = calendar.monthcalendar(year, month)
        num_days = 0
        for week in cal:
            if week[weekday] != 0:
                num_days += 1
        
        print(f"\nThere are {num_days} {weekdays[weekday]}s in {calendar.month_name[month]} {year}.\n")

        # prompt user to run again or exit
        run_program = None
        while(run_program == None):
            run_program = input("Check another month? (y/N) ")
            match run_program.lower():
                case "":
                    run_program = False
                case "exit":
                    run_program = False
                case "n":
                    run_program = False
                case "y":
                    run_program = True
                case _:
                  print ("Invalid response. Please enter 'Y' to repeat or 'N' to exit.")
                  run_program = None
        print()


if __name__ == "__main__":
    main()