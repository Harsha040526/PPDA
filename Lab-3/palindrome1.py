def is_palindrome(string):
    string = string.lower().replace(" ", "")
    left, right = 0, len(string) - 1
    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

string = input("Enter a string: ")
print(is_palindrome(string))