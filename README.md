# 🧠 Math Quiz Game (Command-Line)

A simple Python-based math quiz game to help improve your mental arithmetic skills. The game generates random math problems and tracks how quickly you can solve them.

---

## 🚀 Features

- Randomly generates math problems using addition, subtraction, and multiplication.
- User solves 10 problems per session.
- Measures and displays how long you take to complete the quiz.
- Interactive and beginner-friendly CLI experience.

---

## 📋 How to Use

1. **Clone or download** this repository.
2. **Run the script** using Python:

   ```bash
   python main.py


Press Enter to start the quiz.
Solve each math problem correctly to move on.
Your total time will be shown at the end.

# 🧩 Example Output

Press Enter when you're ready to begin...
#Problem 1 is 7 * 10: 70
#Problem 2 is 10 - 6: 4
...
You completed the quiz in 23.47 seconds.

# 🛠️ Configuration

You can modify these constants in the script to adjust difficulty:

OPERATORS = ['+', '-', '*']  # Allowed operations
MIN_VALUE = 5                # Minimum operand value
MAX_VALUE = 10               # Maximum operand value
MAX_PROBLEMS = 10            # Number of questions per quiz