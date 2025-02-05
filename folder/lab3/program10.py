def is_palindrome(string):
    string = string.lower()
    left, right=0, len(string) - 1
    while right >= left:
       if string[left] != string[right]:
           return False
       left += 1
       right -= 1
    return True
print(is_palindrome('malayalam')) 


user_input = input("Enter a string to check if it's a palindrome: ")
print(is_palindrome(user_input))
