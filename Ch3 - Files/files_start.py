#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # # Open a file for writing and create it if it doesn't exist
    # my_file = open("textfile.txt", "w+")
    
    # # Open the file for appending text to the end
    # my_file = open("textfile.txt", "a+")

    # # write some lines of data to the file
    # for i in range(10):
    #     my_file.write("This is some text\n")
    
    # # close the file when done
    # my_file.close()
    
    # Open the file back up and read the contents
    my_file = open("textfile.txt", "r")
    if my_file.mode == "r":
        # contents = my_file.read()
        # print(contents)
        file_lines = my_file.readlines()
        for line in file_lines:
            print(line)

    
if __name__ == "__main__":
    main()
