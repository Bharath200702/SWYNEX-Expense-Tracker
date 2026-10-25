# SWYNEX Expense Tracker

A beginner-friendly Python command-line application for recording, viewing, and calculating daily expenses.

## Features

- Add expenses with an amount, category, and description.
- Validate user input.
- View all recorded expenses.
- Calculate total spending.
- Save expenses in a JSON file.
- Handle invalid input and file errors.

## Technologies Used

- Python 3
- JSON
- Python standard library

## Project Structure

```text
SWYNEX-Expense-Tracker/
├── main.py
├── expense_utils.py
├── requirements.txt
├── README.md
├── .gitignore
└── expenses.json
```

## Requirements

- Python 3.10 or later recommended.
- Visual Studio Code or another Python editor.
- No third-party Python packages are required.

## Setup Instructions

### 1. Download or clone the project

Clone the repository after uploading it to GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download the project files and open the project folder in VS Code.

### 2. Check Python

Open the terminal and run:

```bash
python --version
```

### 3. Install dependencies

This project uses only Python's standard library, so no external packages need to be installed. The `requirements.txt` file is intentionally empty.

### 4. Run the application

From the project folder, run:

```bash
python main.py
```

## How to Use

1. Select option 1 to add an expense.
2. Enter the amount, category, and description.
3. Select option 2 to view recorded expenses.
4. Select option 3 to calculate total expenses.
5. Select option 4 to exit the application.

## Validation and Error Handling

- Rejects amounts that are invalid or not greater than zero.
- Requires a category and description.
- Handles invalid menu selections.
- Handles JSON loading and file-saving errors.

## Data Storage

Expense records are stored in `expenses.json`. The application loads existing records when it starts and saves new records to the file.

## Learning Outcomes

This project demonstrates Python functions, modular programming, input validation, exception handling, JSON file operations, and project documentation.

## Author

Bharath

Python Internship Project — SWYNEX
