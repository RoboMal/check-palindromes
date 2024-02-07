def check_palindrome(text):
    if text == text[::-1]:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")

text = "racecar"
check_palindrome(text)

