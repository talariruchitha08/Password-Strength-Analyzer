import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character")

    return strength, remarks


def suggest_password():
    return "Try: Strong@1234"


password = input("Enter your password: ")

strength, remarks = check_password_strength(password)

print("\nPassword Strength Score:", strength, "/ 5")

if strength <= 2:
    print("Weak Password")
elif strength <= 4:
    print("Moderate Password")
else:
    print("Strong Password")

if remarks:
    print("\nSuggestions:")
    for r in remarks:
        print("-", r)

print("\nSuggested Password:", suggest_password())