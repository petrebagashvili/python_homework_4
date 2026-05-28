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