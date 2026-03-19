# 🎓 Student Management System (CLI)

## 📌 Overview
This is a Command-Line Interface (CLI) application built in Python. It simulates a lightweight Relational Database Management System (RDBMS) using plain text files (`.txt`). The project demonstrates core backend engineering concepts such as file handling, data mapping, referential integrity, and error handling.

## ✨ Features
* **⚙️ Database Initialization:** Automatically creates the `.database` directory and populates `students.txt` and `grades.txt` with default mock data.
* **📋 Display Records:** Reads and formats all registered students.
* **📊 Subject Reports:** Filters and displays grades for a specific subject or all subjects across all students.
* **🔍 Student Transcripts:** Fetches a specific student's record using their ID and calculates their exact GPA/Average grade.
* **➕ Add New Student:** Appends a new student to the database using an **Auto-Generated Unique ID** (Auto-Increment logic).
* **📝 Add New Grade:** Appends a new grade while enforcing **Referential Integrity** (validates that the student ID exists before adding the grade).
* **🛡️ Defensive Programming:** Features centralized error handling to prevent crashes (e.g., `FileNotFoundError`, `ZeroDivisionError`, and invalid inputs).

## 📂 Project Structure & Database Schema

The system uses two text files to represent a One-to-Many relational schema:

```text
📦 Project Root
 ┣ 📜 lab3.py              # The main executable script
 ┗ 📂 .database            # Auto-generated folder containing the data
   ┣ 📜 students.txt       # Schema: [Primary Key: ID], [Name]
   ┗ 📜 grades.txt         # Schema: [Foreign Key: Student_ID], [Subject], [Grade]
```

## 🚀 How to Run

1. Clone the repository or download the `lab3.py` file.
2. Open your terminal and navigate to the project directory.
3. Run the script using Python 3:
   
   ```bash
   python3 lab3.py
   ```

4. Follow the interactive menu instructions. **Note:** Make sure to select option `1` (Initialize Database) on your first run!

## 🧠 Key Technical Concepts Demonstrated

* **Separation of Concerns:** Distinct helper functions for data retrieval, formatting, and I/O operations.
* **O(1) Data Lookups:** Instead of using nested loops ($O(N \times M)$) to join files, the script loads the primary table into a Python `Dictionary` (Hash Map) for instantaneous foreign-key lookups.
* **State Persistence:** Uses File Streams (`r`, `w`, `a` modes) to ensure data is saved between application sessions.
* **String Formatting:** Uses Python `f-strings` with alignment modifiers (e.g., `:<15`) to generate clean, tabular CLI reports.

---
*Developed as part of the ITI Open Source Applications Development Track.*
