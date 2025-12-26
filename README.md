# Text-to-Python Converter 🤖🐍

> A lightweight, rule-based AI/ML utility that converts natural language instructions into functional Python code.

## 📌 Override
This project was developed as part of an **AI/ML Internship Assessment**. The goal was to build a tool that translates English commands into Python code without relying on heavy external APIs (like OpenAI or Hugging Face), focusing instead on **logic building**, **algorithmic clarity**, and **efficient pattern matching**.

## 🚀 Features
- **Zero Dependencies**: Runs entirely on standard Python libraries.
- **Instant Execution**: No API latency; translates commands in microseconds.
- **Rule-Based Architecture**: Uses robust Regex patterns for deterministic parsing.
- **Extensible**: easy to add new grammar and rules.

## 🛠️ Supported Commands
The current version supports the following instruction patterns:

| Command Type | Example Input | Generated Output |
|--------------|---------------|------------------|
| **Loops** | `print numbers from 1 to 5` | `for i in range(1, 6): print(i)` |
| **Arithmetic** | `add 5 and 10` | `print(5 + 10)` |
| **Variables** | `set x to 10` | `x = 10` |
| **Functions** | `create function foo that prints "bar"` | `def foo(): print('bar')` |
| **Printing** | `print "hello world"` | `print('hello world')` |

## 💻 Installation & Usage

### Prerequisites
- Python 3.x

### Running the Program
1. **Clone the repository**:
   ```bash
   git clone <your-repo-link>
   cd <your-repo-folder>
   ```

2. **Run the converter**:
   ```bash
   python nl_to_python.py
   ```

3. **Interact**:
   Enter your commands when prompted. Type `exit` to quit.
   ```text
   Enter instruction: divide 10 by 2
   Generated Code:
   print(10 / 2)
   ```

## 🧠 Approach & Logic
Instead of a "black box" ML model, this solution uses a transparent **Interpreter Pattern**:
1.  **Input Normalization**: Cleans and standardizes user text.
2.  **Pattern Matching**: Iterates through a prioritized list of Regex rules.
3.  **Code Generation**: Maps captured groups (numbers, variable names) into Python syntax templates.

This ensures **100% accuracy** for supported commands and predictable error handling for unknown inputs.

## 📂 Project Structure
- `nl_to_python.py`: Main logic class `NLPToPython`.
- `verify_solution.py`: Automated test suite.
- `README.md`: Project documentation.

---
*Built with ❤️ by Gunjan Hirani*
