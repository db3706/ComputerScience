my_input = input("Enter a word: ")
rev_input = reversed(my_input) # reverses the input

if list(my_input) == list(rev_input):      # if the word is equal to it's reversed counterpart
    print("The word is a palindrome")      # print that it's a palindrome
else:                                      # if not
    print("The word is not a palindrome")  # print that it's not a palindrome



