
# function prompts user for a string
# checks if that string is a palindrome
def main():
    prompt = "Enter string to test for palindrome or 'exit': "
    while(True):
      test_string = input(prompt)
      if test_string.lower() == "exit":
          break
      else:
          test_string = "".join(filter(lambda ch : ch.isalnum(), test_string))
      print(test_string == test_string[::-1])

if __name__ == "__main__":
    main()