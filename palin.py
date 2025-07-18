def is_palindrome(s):
    # Convert to string in case input is a number
    s = str(s)
    return s == s[::-1]

# Example usage:
input_data = input("Enter a string or number: ")

if is_palindrome(input_data):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
