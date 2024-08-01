test = input("Enter a name: ")

# Remove spaces from the input
test_without_spaces = test.replace(" ", "")

# Calculate and print the length of the input without spaces
print(len(test_without_spaces))