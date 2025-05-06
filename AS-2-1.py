def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = input("Enter a string: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
