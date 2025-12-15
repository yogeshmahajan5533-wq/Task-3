# 🔐 Password Complexity Checker

## 📌 Project Overview
The **Password Complexity Checker** is a Python application that evaluates the strength of a password using common security rules.  
It helps users understand how secure their password is and provides suggestions to improve weak passwords.

This project was developed as **Task-03** for the **Prodigy InfoTech Internship**.

---

## 🎯 Objectives
- Evaluate password strength based on security criteria  
- Classify passwords as **Weak**, **Medium**, or **Strong**  
- Provide user-friendly feedback for improving password security  

---

## 🧠 Password Strength Criteria
The password is checked against the following rules:

1. Minimum length of **8 characters**
2. At least **one uppercase letter (A-Z)**
3. At least **one lowercase letter (a-z)**
4. At least **one numeric digit (0-9)**
5. At least **one special character** (e.g., @, #, $, %, etc.)

Each satisfied condition contributes to the overall strength score.

---

## 🛠️ Technologies Used
- **Python 3**
- **Regular Expressions (re module)**

---

## ▶️ How to Run the Program

1. Make sure Python is installed on your system.
2. Save the Python file (for example: `password_checker.py`).
3. Open a terminal or command prompt.
4. Run the following command:

```bash
python password_checker.py
```

5. Enter a password when prompted.
6. The program will display the password strength and suggestions.

---

## 📊 Strength Classification
| Score | Strength |
|------|----------|
| 5    | Strong   |
| 3–4  | Medium   |
| 0–2  | Weak     |

---

## 📌 Sample Output

```
Enter your password: Abc123@

Password Strength: 🟡 Medium Password

Suggestions to improve your password:
- Password should be at least 8 characters long.
```

---

## 📚 Learning Outcomes
- Understanding of password security principles  
- Practical use of regular expressions  
- Improved logic-building and validation skills  

---

## 🤝 Acknowledgement
Thanks to **Prodigy InfoTech** for providing this opportunity to work on real-world Python tasks and enhance practical programming skills.

---

## 📜 License
This project is created for educational purposes and is free to use.
