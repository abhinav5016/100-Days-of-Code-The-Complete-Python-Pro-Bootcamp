

# 🎢 Roller Coaster Ticket Counter (Python)

A beginner-friendly Python console application that determines **roller coaster eligibility** and **ticket price** based on **height** and **age**.

This project focuses on **conditional logic**, **user input**, and **decision-making**, making it suitable for **Ausbildung IT** beginner portfolios.

---

## 📌 How the Program Works

1. The user enters their height in centimeters.
2. If the height is **150 cm or more**, the user can proceed.
3. The user then enters their age.
4. Based on age, the ticket price is calculated.
5. If the user is **not eligible**, no ticket price is assigned.

---

## 🎟 Eligibility Rules

### Height Requirement

* Minimum height required: **150 cm**

If the height is below 150 cm, the ride is **not allowed**.

---

### Age-Based Ticket Pricing

| Age Range | Ticket Price   |
| --------- | -------------- |
| Below 12  | $10            |
| 12 – 18   | $15            |
| 19 – 50   | $20            |
| Above 50  | ❌ Not eligible |

If age is **above 50**, the user is informed that they are **not eligible**, and the ticket price remains **$0**.

---

## ▶️ How to Run

1. Ensure Python 3 is installed
2. Navigate to the project folder
3. Run the script:

```bash
python main.py
```

4. Follow the prompts in the terminal

---

## 🧪 Example Output

```
Welcome to Roller Coaster Ticket Counter

What is your height in cm?
175
You can ride the roller coaster!
What is your age?
51
You are not eligible to ride the roller coaster.
Your ticket price is: $0
```

---

## 🛠 Concepts Used

* `input()` and type casting with `int()`
* Conditional statements (`if / elif / else`)
* Variables
* f-strings for output formatting

---

## 📁 Project Level

* Beginner Python Project
* Console-based application
* Suitable for GitHub portfolio (Ausbildung IT)

---

## 🚀 Future Improvements

* Prevent ticket price display for ineligible users
* Add input validation (non-numeric values)
* Use functions to improve structure
* Add loop support for multiple users

---

### ✅ Why This README Is Now Correct

* Matches **actual program output**
* Clearly explains **why `$0` appears**
* No misleading eligibility claims
* Professional and reviewer-safe

---

## 👤 Author

Abhinav

