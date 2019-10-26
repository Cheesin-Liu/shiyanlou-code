# I code this palindrome.py by myself
s = input("Please enter a string: ")
n = len(s)
print("The length of string is {}".format(n))
i = 0
while i < n:

    if s[i] == s[-(i+1)]:
        i += 1
    else:
        print("The string is not a palindrome")
        break
    if i == n:
        print(("The string is a palindrme"))

