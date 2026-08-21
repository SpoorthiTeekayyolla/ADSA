# task.py

def Check_Palindrome(n: int, s: str) -> bool:

    # Helper function to check if a string is palindrome
    def is_palindrome(text):
        return text == text[::-1]

    # If already a palindrome
    if is_palindrome(s):
        return True

    # Try deleting each character once
    for i in range(n):
        new_string = s[:i] + s[i+1:]

        if is_palindrome(new_string):
            return True

    return False


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))