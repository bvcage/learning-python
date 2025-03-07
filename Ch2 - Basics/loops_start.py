#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while(x < 5):
        print(x)
        x += 1


    # TODO: define a for loop
    for i in range(x):
        print(i)


    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for day in days:
        print(day)


    # TODO: use the break and continue statements
    for x in range(5, 10):
        if x == 7:
            break
        print(x)

    for x in range(5, 10):
        if x % 2 == 0:
            continue
        print(x)


    # TODO: using the enumerate() function to get index 
    for index, day in enumerate(days):
        print(index, day)
    
  
if __name__ == "__main__":
    main()
