# SQL-Backed Library Inventory Management System

A robust console application built in Python integrated with an SQLite database engine to manage a real-time book inventory lifecycle. The application replaces standard text-file storage with structural, relational SQL queries to safely process transactional records.

## Key Engineering Features
* **Relational Database Integration:** Designed a local relational storage engine using Python's native `sqlite3` driver, implementing structured schemas with primary key autoincrementation rules.
* **State Modifying Transactions:** Authored optimized SQL `UPDATE` queries linked with conditional filter clauses (`WHERE id = ? AND status = ?`) to handle real-time check-out/check-in record workflows safely.
* **Defensive Input Handling:** Engineered numeric parsing checkpoints (`.isdigit()`) and tuple parameter binding variables (`?`) to completely eliminate terminal crashes and secure the database against runtime data injection vulnerabilities.

## Technology Stack
* **Language:** Python 3.x
* **Database Engine:** SQLite3 (Relational Database Management System)

## How To Run Locally
1. Clone or download this repository.
2. Launch your terminal/command prompt and navigate into the project workspace directory.
3. Run the following deployment command:
   ```bash
   python Library.py
