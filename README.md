# Stock Portfolio Tracker

## CodeAlpha Internship Task
**CodeAlpha Python Programming Internship — Task 2: Stock Portfolio Tracker**

## Project Description
A simple console-based Python program that calculates the total value
of a stock portfolio. The user enters stock symbols and quantities, and
the program looks up each stock's price from a manually defined
(hardcoded) dictionary, calculates the investment value, and displays a
full portfolio summary with an optional file export.

> **Important:** All stock prices in this project are manually defined
> sample prices for educational purposes. They are **not** real-time or
> live market prices, and this tool does not connect to any stock market
> API or data source.

## Features
- Displays all available stock symbols and their sample prices.
- Accepts one or more stock entries per session.
- Validates stock symbols against the predefined dictionary.
- Validates quantities (rejects empty input, non-numeric input, zero,
  and negative numbers).
- Calculates investment value per stock as `price × quantity`.
- Displays a clean, formatted portfolio summary with a grand total.
- Optionally saves the summary to a `.txt` or `.csv` file.
- Case-insensitive stock symbol entry (e.g., `aapl` and `AAPL` both work).

## Technologies Used
- **Python 3** (standard library only)
- `csv` module — for optional CSV export
- No external packages, no GUI, no APIs, no live data

## Python Concepts Demonstrated
- **Dictionary** — `STOCK_PRICES` stores each stock symbol and its price
- **Input/Output** — reading user input, printing formatted results
- **Basic arithmetic** — `investment = price * quantity`
- **File handling (optional)** — writing the summary to `.txt` or `.csv`
- **Functions** — the program is split into small, single-purpose functions
- **Loops and conditionals** — used for input validation and repeated entries

## How the Program Works
1. Displays a welcome message and a disclaimer about sample prices.
2. Shows the list of available stock symbols and their prices.
3. Asks for a stock symbol and validates it against the dictionary.
4. Asks for a quantity and validates that it's a positive whole number.
5. Calculates the investment value for that entry.
6. Asks if the user wants to add another stock (repeats steps 3–5 if yes).
7. Displays a summary table of every entry and the total investment value.
8. Asks if the user wants to save the result to a file.
9. If yes, asks for `.txt` or `.csv` format and writes the file.
10. Ends with a closing message.

## Example Usage
```
=============================================
     STOCK PORTFOLIO TRACKER
=============================================
Note: Stock prices below are manually defined
sample prices, not real-time market prices.

Available stocks:
  AAPL   - $180
  TSLA   - $250
  GOOGL  - $140
  ...

Enter stock symbol: AAPL
Enter quantity: 10
Added: 10 share(s) of AAPL at $180 each.

Add another stock? (yes/no): no

=============================================
     PORTFOLIO SUMMARY
=============================================
Symbol  Quantity  Price     Investment
---------------------------------------------
AAPL    10        $180      $1800
---------------------------------------------
Total Investment Value: $1800
=============================================

Save portfolio to a file? (yes/no): no

Thank you for using Stock Portfolio Tracker. Goodbye!
```

## Project Structure
```
CodeAlpha_Stock_Portfolio_Tracker/
├── stock_portfolio_tracker.py   # main program
├── README.md                    # project documentation
├── requirements.txt             # dependency list (standard library only)
└── .gitignore
```

## How to Run
```
python stock_portfolio_tracker.py
```

## File-Saving Functionality
After viewing the portfolio summary, you can choose to save it:
- **`.txt`** — a plain-text summary with each stock's details and the total.
- **`.csv`** — a spreadsheet-friendly table with columns for symbol,
  quantity, price, and investment, plus a total row.

The file is saved as `portfolio_result.txt` or `portfolio_result.csv`
in the same folder as the script.

## Learning Concepts Demonstrated
- Using a dictionary to store and look up fixed reference data.
- Structuring a program into small, testable functions.
- Validating user input to prevent crashes from bad data.
- Performing basic arithmetic to compute derived values.
- Writing formatted output to the console and to a file.
- Working with two simple file formats (`.txt` and `.csv`).

## Author
**Name:** [Your Name Here]
**Internship:** CodeAlpha Python Programming Internship
**Task:** Task 2 — Stock Portfolio Tracker
