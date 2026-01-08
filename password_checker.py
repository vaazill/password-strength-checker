import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password)
    lower_criteria = re.search(r"[a-z]", password)
    digit_criteria = re.search(r"[0-9]", password)
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([
        length_criteria,
        bool(upper_criteria),
        bool(lower_criteria),
        bool(digit_criteria),
        bool(special_criteria)
    ])

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

password = input("Enter a password to check strength: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")