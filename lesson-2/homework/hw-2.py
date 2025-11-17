import random
import string

name = input("Enter your name: ")
birthyear = int(input("Enter your birth year: "))
age = 2025 - birthyear
print(f"Hello {name}, your age is {age}")

txt = 'LMaasleitbtui'
print("Even indices:", txt[0::2])
print("Odd indices:", txt[1::2])

txt = 'MsaatmiazD'
print("Every second character:", txt[::2])
print("Every second character reversed:", txt[::-2])

txt = "I'am John. I am from London"
residence = txt.split("from ")[1]
print("Residence:", residence)

text_to_reverse = input("Enter some text: ")
print("Reversed:", text_to_reverse[::-1])

some_text = input("Enter text to count vowels: ")
vowels = 'aeiouAEIOU'
num_vowels = sum(some_text.count(v) for v in vowels)
print("Number of vowels:", num_vowels)

numbers = input("Enter numbers separated by space: ")
numbers_list = [int(n) for n in numbers.split()]
print("Maximum number:", max(numbers_list))

word = input("Enter a word: ")
if word.lower() == word.lower()[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

email = input("Enter your email: ")
domain = email.split("@")[1]
print("Email domain is:", domain)

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Your random password is:", password)
