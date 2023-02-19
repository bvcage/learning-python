#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is", today)

    # TODO: print out the date's individual components
    print("Today's date components:")
    print("  day:", today.day)
    print("  month:", today.month)
    print("  year:", today.year)
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print("Today's weekday number is", today.weekday(), "which is a", days[today.weekday()])
    
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is", today)
    
    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("The current time is",t)

 

  
if __name__ == "__main__":
    main()
  