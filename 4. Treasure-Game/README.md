

# 🏝️ Treasure Island – Text-Based Adventure Game (Python)

A story-driven, decision-based **text adventure game** built in Python.
Every choice matters. Mistakes persist. Survival depends on logic, not luck.

This project demonstrates **control flow, state management, and user interaction** using core Python concepts.

---

## 🎮 Game Overview

You are an explorer entering an ancient temple that **remembers every mistake**.
Your decisions influence:

* The story path
* Your physical condition
* Whether the treasure can be claimed

There are **multiple stages**, **branching paths**, and **persistent injuries** that affect later gameplay.

---

## 🧠 Core Mechanics

* **Input-based decision system**
* **Persistent state tracking**

  * `injured_arms`
  * `injured_lungs`
* **Logical consequences**
* **Multiple endings**

  * Full victory
  * Partial survival
  * Death

---

## 🗺️ Game Stages

### Stage 1 – Symbols of Fate

Choose between **Light** and **Void**
Wrong choices trigger traps and permanent injuries.

### Stage 2 – The Poisoned Hall

Door selection leads to either safety or a gas-filled room.
Survival may cost lung damage.

### Stage 3 – The Broken Bridge

Your **previous injuries matter**.
Jumping may be impossible if weakened.

### Final Stage – The Vault

The final seal depends on:

* Your **choices**
* Your **injury status**

Only logical alignment unlocks the treasure.

---

## 🏆 Possible Endings

* ✅ **True Victory** – No injuries + correct final seal
* ⚖️ **Earned Victory** – Injured but wise final choice
* ❌ **Survival Only** – Escape without treasure
* ☠️ **Game Over** – Death due to poor decisions

---

## 🛠️ Concepts Used

* `if / elif / else`
* Boolean state tracking
* Nested decision trees
* String handling
* Program termination (`exit()`)

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Save the file as `main.py`
3. Run the game:

```bash
python main.py
```

Follow the on-screen prompts and type your choices.

---

## 📂 Project Structure

```
Treasure-Game/
│
├── main.py
└── README.md
```


## 🚀 Future Improvements (Optional)

* Restart loop instead of exiting
* Input validation
* Inventory system
* ASCII art visuals
* Modular functions

---

## 👤 Author

Abhinav