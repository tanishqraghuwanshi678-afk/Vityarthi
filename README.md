Campus Lost & Found System

A Python-based console application designed to help students and faculty report, track, and review lost or found items on campus.
This simple yet effective tool demonstrates how data can be organized using Python dictionaries and lists within a menu-driven interactive program.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.x-blue.svg" /> <img src="https://img.shields.io/badge/Status-Active-brightgreen" /> <img src="https://img.shields.io/badge/License-MIT-lightgrey" /> </p>
📑 Table of Contents

About the Project

Key Features

Project Screenshots

How the System Works

Folder Structure

Installation

How to Run

Code Explanation

Use Cases

Future Improvements

Contributing

📘 About the Project

The Campus Lost & Found System is a lightweight Python application meant to solve a simple yet common issue: misplaced belongings on campus.
Instead of relying on manual logs or scattered information, this tool provides a structured way to record and view lost/found items in one place.

This project is perfect for:

Beginner Python developers

Students learning basic data structures

Mini-project or assignment submissions

Demonstrations of menu-driven programs

🌟 Key Features

✔ Add lost or found items
✔ View all submitted entries
✔ Store item name, location, and contact
✔ Simple, readable code
✔ Beginner-friendly Python logic
✔ Runs entirely from the console
✔ No external libraries required

🖼 Project Screenshots

You can replace these with actual screenshots later.

===== Campus Lost & Found System =====
1. Add Lost/Found Item
2. View All Items
3. Exit
Enter your choice:

--- Lost & Found Items ---
1. Wallet - Library (Contact: 9876543210)
2. Water Bottle - Canteen (Contact: 9123456789)

🛠 How the System Works

The program uses a while True loop to display a menu with three choices:

1. Add Lost/Found Item

Prompts the user for:

Item name

Place where lost/found

Contact information

Then stores the data inside a list of dictionaries.

2. View All Items

Shows every recorded item in a neat, numbered list.

3. Exit

Safely terminates the program.

📁 Folder Structure
Campus-Lost-And-Found-System/
│
├── src/
│   └── lost_found.py
│
├── docs/
│   └── statement.md
│
├── README.md
├── LICENSE
└── .gitignore

🧩 Installation
Step 1 — Clone the repository
git clone https://github.com/your-username/campus-lost-found.git

Step 2 — Navigate to the folder
cd campus-lost-found

Step 3 — Make sure Python is installed
python --version

▶️ How to Run

Run the script with:

python src/lost_found.py


Or, depending on your OS:

python3 src/lost_found.py

🧠 Code Explanation (High-Level)
🟦 Data Structure

The items are stored as:

{
    "item": "Wallet",
    "place": "Library",
    "contact": "9876543210"
}

🟩 Main Components

List (lost_items) to store items

Dictionary for each item’s details

Menu loop for interaction

Conditionals for each user choice

🟨 Example Code Snippet
lost_items = []

while True:
    print("\n===== Campus Lost & Found System =====")
    print("1. Add Lost/Found Item")
    print("2. View All Items")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        place = input("Enter place where lost/found: ")
        contact = input("Enter your contact: ")

        lost_items.append({
            "item": item,
            "place": place,
            "contact": contact
        })

        print("\nItem added successfully!")

    elif choice == "2":
        print("\n--- Lost & Found Items ---")
        if len(lost_items) == 0:
            print("No items added yet.")
        else:
            for i, it in enumerate(lost_items, start=1):
                print(f"{i}. {it['item']} - {it['place']} (Contact: {it['contact']})")

    elif choice == "3":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")

🎯 Use Cases

This project can be used for:

School or college lost-and-found desks

Mini-project submissions

Learning how to manage user input

Understanding loops and dictionaries

Command-line application practice

🚀 Future Improvements

Here are planned enhancements:

 Save items to a text or JSON file

 Add search functionality

 Add item deletion or editing

 Add categories (electronics, documents, personal items, etc.)

 GUI version using Tkinter

 Web version using Flask or Django

 Mobile version using Kivy

🤝 Contributing

Contributions are welcome!
Feel free to:

Submit issues

Open pull requests

Suggest enhancements

Report bugs

Please follow standard GitHub etiquette.
