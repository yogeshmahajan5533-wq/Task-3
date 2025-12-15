import re

def check_password(password):
    issues = []
    score = 0
    
    length_ok  = len(password) >= 8
    upper_ok   = re.search(r"[A-Z]", password)
    lower_ok   = re.search(r"[a-z]", password)
    digit_ok   = re.search(r"[0-9]", password)
    symbol_ok  = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    for condition in [length_ok, upper_ok, lower_ok, digit_ok, symbol_ok]:
        if condition:
            score += 1

    if not length_ok:
        issues.append("• Password should have at least 8 characters.")
    if not upper_ok:
        issues.append("• Add at least one uppercase letter (A–Z).")
    if not lower_ok:
        issues.append("• Add at least one lowercase letter (a–z).")
    if not digit_ok:
        issues.append("• Add at least one digit (0–9).")
    if not symbol_ok:
        issues.append("• Include at least one special character (!@#$...).")

    if score == 5:
        strength = "Strong Password 🔐"
    elif score >= 3:
        strength = "Moderate Password 🟡"
    else:
        strength = "Weak Password 🔴"

    return strength, issues


#  MAIN PROGRAM 
print(" --- Password Strength Checker --- ")
pwd = input("Enter your password: ")

strength, problems = check_password(pwd)

print("\nPassword Strength:", strength)
print("\nFeedback:")
if problems:
    for msg in problems:
        print(msg)
else:
    print("✔ Your password meets all requirements!")

print()    
