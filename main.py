# სავარჯიშო 1
import random
import string


def password_generator():
    while True:
        length_input = input("Enter password length: ")
        if not length_input.isdigit():
            print("Enter numbers only!")
            continue  # თავიდან აწყებინებს ციკლს

        length = int(length_input)

        use_upper = input("Do you want uppercase letters? (yes/no): ").lower()
        use_lower = input("Do you want lowercase letters? (yes/no): ").lower()
        use_digits = input("Do you want numbers? (yes/no): ").lower()
        use_symbols = input("Do you want symbols? (yes/no): ").lower()

        if use_upper not in ["yes", "no"] or use_lower not in ["yes", "no"] or use_digits not in ["yes",
                                                                                                  "no"] or use_symbols not in [
            "yes", "no"]:
            print("Enter only yes or no!")
            continue

        all_chars = ""
        if use_upper == "yes": all_chars += string.ascii_uppercase
        if use_lower == "yes": all_chars += string.ascii_lowercase
        if use_digits == "yes": all_chars += string.digits
        if use_symbols == "yes": all_chars += string.punctuation

        if all_chars == "":
            print("Choose at least one option!")
            continue

        password = "".join(random.choice(all_chars) for _ in range(length))
        print("Generated password:", password)

        stop = input("Do you want another password? (yes/no): ").lower()
        if stop == "no":
            print("Thank you!, goodbye!")
            return password  # აბრუნებს პაროლს და ასრულებს ფუნქციას
        elif stop == "yes":
            print("Thank you for using this program again")
        else:
            print("Invalid input, exiting generator.")
            return password
password_generator()


# სავარჯიშო 2
testpass = input("თუ გინდა საცდელად გამოიყენე ჩვენ მიერ გენერირებული პაროლი (yes/no): ").lower()

if testpass == "yes":
    password = password_generator()
else:
    password = input("შეიყვანე პაროლი: ")

if not password:
    print("პაროლი ცარიელია!")
    exit()

score = 0

if len(password) >= 8: score += 2
if any(char.isdigit() for char in password): score += 2
if any(char.isupper() for char in password): score += 2
if any(char.islower() for char in password): score += 2
if any(not char.isalnum() for char in password): score += 2

if len(set(password)) < len(password) / 2:
    score -= 2

score = max(0, min(score, 10))

print("\nპაროლის ქულა:", score, "/10")

if score <= 4:
    print("სტატუსი: weak ")
elif score <= 7:
    print("სტატუსი: medium ")
else:
    print("სტატუსი: strong ")
# სავარჯიშო 3

def fibonacci(length):
    if length == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

loop = True
while loop:
    user_input = input("შეიყვანე რიცხვი: ")


    if user_input.isdigit():
        number = int(user_input)

        if number <= 0:
            print("შეიყვანე დადებითი რიცხვი (0-ზე მეტი)!")
        else:
            print("ფიბონაჩის რიგი:", fibonacci(number))
            stop = input("გინდათ ახლიდან ცდა? (yes/no): ").lower()
            if stop == "no":
                print("Thank you!")
                loop = False
            else:
                loop = True

    else:
        print("შეცდომა! გთხოვთ შეიყვანოთ მხოლოდ მთელი დადებითი რიცხვი.")

#  სავარჯიშო 4

def is_palindrome(s):
    return s == s[::-1]

def closest_palindrome(s):
    for i in range(len(s)):
        candidate = s[:i] + s[i+1:]
        if is_palindrome(candidate):
            return candidate

    for i in range(len(s)):
        candidate = s[:i] + s[i] + s[i:]
        if is_palindrome(candidate):
            return candidate

    return s[::-1]


text = input("Enter text: ")

if not text.isalnum():
    print("Only letters and numbers allowed!")
else:
    if is_palindrome(text):
        print("It is a palindrome")
    else:
        print("Not a palindrome")
        print("Closest palindrome suggestion:", closest_palindrome(text))

# სავარჯიშო 5

import random

word = input("Enter one word only: ")

if len(word.split()) != 1 or not word.isalpha():
    print("Invalid input! Only one word allowed.")
else:
    nicknames = [
        word + "Master",
        word + "Pro",
        "Emperor_" + word,
        word + "X",
        word + "_King"
    ]

    print("Nicknames:")
    for n in random.sample(nicknames, 5):
        print(n)

# სავარჯიშო 6

import random

numbers = input("Enter numbers separated by space: ")

nums = numbers.split()

if not all(n.lstrip("-").isdigit() for n in nums):
    print("Only numbers allowed!")
else:
    nums = [int(n) for n in nums]

    print("Choose sorting type:")
    print("1 - ზრდადობით")
    print("2 - კლებადობით")
    print("3 - რანდომულად")
    print("4 - მხოლოდ უნიკალური მონაცემები დატოვოს")

    choice = input("Enter choice: ")

    if choice == "1":
        print(sorted(nums))

    elif choice == "2":
        print(sorted(nums, reverse=True))

    elif choice == "3":
        random.shuffle(nums)
        print(nums)

    elif choice == "4":
        unique_nums = list(dict.fromkeys(nums))
        print(unique_nums)

    else:
        print("Invalid choice")

# სავარჯიშო 7

def filter_text(text):
    result = ""

    for char in text:
        if char.isalpha() or char == " ":
            result += char

    return result


text = input("Enter text: ")
print("Filtered text:", filter_text(text))

# სავარჯიშო 8

nums = input("Enter numbers separated by space: ").split()

if not all(n.lstrip("-").isdigit() for n in nums):
    print("Only numbers allowed!")
else:
    row = [int(n) for n in nums]

    print("Pyramid:")
    print(*row)

    while len(row) > 1:
        new_row = []

        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])

        print(*new_row)
        row = new_row

# სავარჯიშო 9

text = input("Enter text: ").lower()

words = text.split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

max_count = max(freq.values())
most_common = [word for word, count in freq.items() if count == max_count]

print("Most frequent word(s):", most_common)

# სავარჯიშო 10

sentence = input("Enter sentence: ")

words = sentence.split()

result = {}

for word in words:
    result[word] = len(word)
print(result)

# #####################################
print("ALL HOMEWORK DONE")