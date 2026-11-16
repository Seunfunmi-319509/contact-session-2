# Python Learning Session – Assignments

## Overview

This repository contains three Python assignments completed during one learning session. The assignments focus on file handling, working with file paths, regular expressions, sorting algorithms, and searching algorithms.

Each task builds on Python concepts and practical problem-solving skills.

## Project Structure

```text
contact-session-2/
│
├── name_extraction.py
├── name.txt
│
├── print_path.py
│
├── baby_names.py
├── baby2008.html
│
└── README.md
```

## Assignment 1: Name Extraction

**File:** `name_extraction.py`

### Objective
Read a full name from a text file, extract the individual names, and print each name on a separate line.

### Concepts Practised
- File handling using `open()`
- Reading file contents using `.read()`
- String manipulation using `.split()`
- Conditional statements (`if` and `else`)
- Accessing list elements using indexes

### How It Works
1. Opens `name.txt` and reads its contents.
2. Splits the full name into individual words.
3. Checks whether the file contains exactly three names.
4. Assigns the names to first name, middle name, and last name.
5. Prints each name on a separate line.
6. Displays an error message if the file does not contain exactly three names.

### How to Run

```bash
python name_extraction.py
```

**Note:** Ensure that `name.txt` exists in the project directory and contains a full name with three parts.

---

## Assignment 2: Print Path

**File:** `print_path.py`

### Objective
Explore Python's file path handling capabilities by displaying the current working directory and the absolute path of a specified file.

### Concepts Practised
- Importing Python modules
- Working with the `os` module
- Using `os.getcwd()`
- Using `os.path.abspath()`
- Understanding relative and absolute file paths

### How It Works
1. Imports Python's built-in `os` module.
2. Uses `os.getcwd()` to display the current working directory.
3. Uses `os.path.abspath()` to display the absolute path of `print_path.py`.

### How to Run

```bash
python print_path.py
```

---

## Assignment 3: Baby Names Extraction, Sorting and Searching

**File:** `baby_names.py`

### Objective
Extract male and female baby names from an HTML file using Regular Expressions, implement a sorting algorithm to arrange the names alphabetically, and implement Binary Search to find a name in the sorted list.

### Concepts Practised
- File handling and reading HTML files
- Regular Expressions using Python's `re` module
- Pattern matching and capturing groups
- Lists and tuple unpacking
- Bubble Sort algorithm
- Binary Search algorithm
- Loops and conditional statements
- Case-insensitive string comparison using `.casefold()`

### How It Works

**1. Name Extraction**
- Reads the contents of `baby2008.html`.
- Uses `re.findall()` and a regular expression to extract male and female baby names.
- Stores the extracted names in a Python list.

**2. Sorting**
- Implements the Bubble Sort algorithm to arrange the names alphabetically.
- Compares adjacent names and swaps them when necessary.

**3. Searching**
- Implements Binary Search to locate a name in the sorted list.
- Uses `low`, `high`, and `mid` to determine the search position.
- Uses `.casefold()` to make the search case-insensitive.
- Displays whether the requested name was found.

### How to Run

```bash
python baby_names.py
```

**Note:** Ensure that `baby2008.html` is in the same project directory as the Python script.

---

## Technologies and Tools

- **Programming Language:** Python
- **Modules:** `re`, `os`
- **Algorithms:** Bubble Sort and Binary Search
- **File Formats:** `.py`, `.txt`, `.html`

## Learning Outcomes

Through these assignments, I gained practical experience in:

- Reading and processing data from external files.
- Extracting information using Regular Expressions.
- Understanding and working with file paths.
- Manipulating strings and lists.
- Implementing sorting and searching algorithms without relying on Python's built-in sorting and searching methods.
- Applying logical thinking to solve programming problems.

---

**Author:** Oluwaseun Showunmi

**Purpose:** Python Programming Learning Session – Practical Assignments