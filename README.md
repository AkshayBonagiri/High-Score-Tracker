# 🎯 Random Score High Score Tracker

## 📌 Project Description
This is a beginner-friendly Python project that generates a random score between 1 and 100 and saves the **highest score** in a text file (`Hi_score.txt`). Each time the program runs, it compares the new score to the previous high score and updates it if the new score is higher.

The project demonstrates working with **random numbers**, **file handling**, and **basic conditional logic** in Python.

## 🧑‍💻 What I Learned
- ✅ **File Handling (I/O)** in Python using `open()`, `read()`, and `write()`
- ✅ How to **read from** and **write to** a file
- ✅ How to **store persistent data** (high scores) across multiple runs of a program
- ✅ **Random number generation** using `random.randint()`
- ✅ Using **if-else conditions** to update values based on comparisons
- ✅ **Type conversion** between strings and integers (`int()` and `str()`)

## 🚀 How it Works
1. Generates a random score between **1 and 100**.
2. Reads the current **high score** from `Hi_score.txt`.
3. If the current score is **greater than the high score**, it overwrites the file.
4. Prints your score in the terminal.

## 🗂️ Project Files
- `main.py` → Main Python script with the game logic.
- `Hi_score.txt` → Text file that stores the **highest score**.

## ▶️ Usage
Run the program using:
```bash
python main.py
