#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

def main():
    print("Hello, world!")
    name = input("What is your name? ")
    name = name.capitalize()
    print(f"Nice to meet you, {name}!")

# run main() if file executed as a program
if __name__ == "__main__":
    main()