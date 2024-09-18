def palindrome(s):
     return s==s[::-1]

word=str(input("enter the word"))
if palindrome:
     print("the word is palindrome")
else:
     print("the word is not palindrome")