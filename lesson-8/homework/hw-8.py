
# 1. ZeroDivisionError

try:
    a = int(input("1) Enter a number: "))
    b = int(input("1) Enter another number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# 2. Raise ValueError

user_input = input("\n2) Enter an integer: ")
try:
    num = int(user_input)
    print("Valid integer:", num)
except ValueError:
    raise ValueError("Invalid input! Expected an integer.")


# 3. FileNotFoundError

try:
    file = open("myfile.txt", "r")
    print("\n3) File content:\n", file.read())
    file.close()
except FileNotFoundError:
    print("Error: File does not exist!")


# 4. Raise TypeError

x = input("\n4) Enter first number: ")
y = input("4) Enter second number: ")

try:
    x = float(x)
    y = float(y)
    print("Sum =", x + y)
except ValueError:
    raise TypeError("Non-numeric input detected!")


# 5. PermissionError

try:
    f = open("/root/secret.txt", "r")
    print(f.read())
    f.close()
except PermissionError:
    print("\n5) Permission denied!")


# 6. IndexError

my_list = [10, 20, 30]

try:
    index = int(input("\n6) Enter index: "))
    print(my_list[index])
except IndexError:
    print("Error: Index out of range!")


# 7. KeyboardInterrupt

try:
    num = input("\n7) Enter a number (Ctrl+C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")


# 8. ArithmeticError

try:
    a = float(input("\n8) Enter a number: "))
    b = float(input("8) Enter another number: "))
    print(a / b)
except ArithmeticError:
    print("Arithmetic error occurred!")


# 9. UnicodeDecodeError

try:
    with open("data.txt", "r", encoding="ascii") as f:
        print("\n9) File content:", f.read())
except UnicodeDecodeError:
    print("Error: Encoding problem reading file.")


# 10. AttributeError

my_list = [1, 2, 3]

try:
    my_list.non_existing_method()
except AttributeError:
    print("\n10) Error: Attribute does not exist.")


# 11. Read entire file

try:
    with open("file.txt", "r") as f:
        print("\n11) Entire file:\n", f.read())
except:
    print("\n11) file.txt not found.")


# 12. First n lines

try:
    n = int(input("\n12) Enter n: "))
    with open("file.txt") as f:
        for i in range(n):
            print(f.readline(), end="")
except:
    print("12) file.txt missing.")


# 13. Append text to file

text = input("\n13) Enter text to append: ")
with open("file.txt", "a") as f:
    f.write(text + "\n")

with open("file.txt") as f:
    print("\n13) Updated file:\n", f.read())


# 14. Last n lines

n = int(input("\n14) Enter n: "))
with open("file.txt") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))

# 15. File → list

with open("file.txt") as f:
    lines = f.readlines()
print("\n15) List:", lines)


# 16. File → variable

content = ""
with open("file.txt") as f:
    for line in f:
        content += line
print("\n16) Variable:\n", content)

# ================================
# 17. File → array

arr = []
with open("file.txt") as f:
    for line in f:
        arr.append(line.strip())
print("\n17) Array:", arr)


# 18. Longest words

with open("file.txt") as f:
    words = f.read().split()
print("\n18) Longest word:", max(words, key=len))

# ================================
# 19. Count lines
# ================================
with open("file.txt") as f:
    print("\n19) Line count:", len(f.readlines()))


# 20. Word frequency

from collections import Counter
with open("file.txt") as f:
    words = f.read().replace(",", " ").split()
print("\n20) Word frequency:", Counter(words))


# 21. File size

import os
print("\n21) File size:", os.path.getsize("file.txt"), "bytes")


# 22. Write list to file

items = ["apple", "banana", "orange"]
with open("output.txt", "w") as f:
    for item in items:
        f.write(item + "\n")
print("\n22) output.txt created")

# 23. Copy file

with open("file.txt") as s, open("dest.txt", "w") as d:
    d.write(s.read())
print("\n23) dest.txt created")


# 24. Combine lines from two files

try:
    with open("file1.txt") as f1, open("file2.txt") as f2:
        print("\n24) Combined:")
        for a, b in zip(f1, f2):
            print(a.strip(), b.strip())
except:
    print("\n24) file1.txt or file2.txt missing")


# 25. Random line

import random
with open("file.txt") as f:
    lines = f.readlines()
print("\n25) Random line:", random.choice(lines))


# 26. Check if file is closed

f = open("file.txt")
print("\n26) Is closed? (before):", f.closed)
f.close()
print("26) Is closed? (after):", f.closed)


# 27. Remove newline characters

with open("file.txt") as file:
    clean = [line.strip() for line in file]
print("\n27) Cleaned list:", clean)


# 28. Count words

with open("file.txt") as f:
    words = f.read().replace(",", " ").split()
print("\n28) Word count:", len(words))


# 29. Extract characters from files

chars = list()
try:
    for filename in ["a.txt", "b.txt", "c.txt"]:
        with open(filename) as f:
            chars.extend(list(f.read()))
    print("\n29) Characters:", chars)
except:
    print("\n29) Some files missing (a.txt, b.txt, c.txt)")


# 30. Generate A–Z files

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}\n")
print("\n30) A–Z files generated.")

# 31. Alphabet with N letters per line
n = int(input("\n31) Letters per line: "))
alphabet = string.ascii_lowercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), n):
        f.write(alphabet[i:i+n] + "\n")

print("31) alphabet.txt created.")
      
