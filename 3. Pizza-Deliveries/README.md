

# 🍕 Pizza Deliveries (Python)

A beginner-friendly Python console application that calculates the final price of a pizza based on **size**, **pepperoni**, and **extra cheese** selections.

This project is intended to practice **conditional logic**, **user input**, and **basic price calculation** in Python.

---

## 📌 Features

* Choose pizza size (Small, Medium, Large)
* Option to add pepperoni
* Option to add extra cheese
* Displays the final bill amount
* Stops execution if an invalid size is selected

---

## 🧠 How the Program Works

1. The user selects a pizza size (`S`, `M`, or `L`)
2. The user chooses whether to add pepperoni
3. The user chooses whether to add extra cheese
4. The program calculates and prints the final price

If an invalid pizza size is entered, the program displays an error message and exits.

---

## 💵 Pricing Rules

### Base Price

| Size       | Price |
| ---------- | ----- |
| Small (S)  | $15   |
| Medium (M) | $20   |
| Large (L)  | $25   |

### Add-ons

* Pepperoni

  * Small pizza: +$2
  * Medium or Large pizza: +$3
* Extra cheese: +$1

---

## ▶️ Example Output

```
Welcome to Pizza Deliveries!

What size pizza do you want? S, M, or L
l
Do you want pepperoni? Y or N
y
Do you want extra cheese? Y or N
y

Your final bill is: $29
```

---

## 🛠 Concepts Used

* User input with `input()`
* Conditional statements (`if / elif / else`)
* Variables and arithmetic operations
* f-strings for formatted output

---

## ▶️ How to Run

1. Ensure Python 3 is installed
2. Open a terminal in the project directory
3. Run the program:

```bash
python main.py
```

---

## 📁 Project Level

* Beginner Python project
* Console-based application

---

## 🚀 Possible Improvements

* Validate `Y / N` inputs
* Re-prompt user instead of exiting
* Handle extra spaces using `.strip()`
* Convert logic into functions

---

## 👤 Author

Abhinav


