# Billing Management Project

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("billing.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bills (
    user_id INTEGER,
    month TEXT,
    amount INTEGER
)
""")

# Insert sample users (only once)
users = [(i, f"User_{i}") for i in range(1, 21)]
cursor.executemany("INSERT OR IGNORE INTO users VALUES (?, ?)", users)

# Check if bills already exist
cursor.execute("SELECT COUNT(*) FROM bills")
count = cursor.fetchone()[0]

months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Insert bills only if empty
if count == 0:
    import random
    for user_id in range(1, 21):
        for month in months_list:
            amount = random.randint(1000, 5000)
            cursor.execute("INSERT INTO bills VALUES (?, ?, ?)", (user_id, month, amount))
    conn.commit()

# Fetch user data

def fetch_user(user_id):
    cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()

    if not user:
        print("User not found")
        return

    print(f"\nBilling Details for {user[0]}\n")

    cursor.execute("SELECT month, amount FROM bills WHERE user_id=?", (user_id,))
    data = cursor.fetchall()

    months = [row[0] for row in data]
    amounts = [row[1] for row in data]

    for m, a in data:
        print(f"{m}: ₹{a}")

    plt.figure()
    plt.bar(months, amounts)
    plt.title(f"Monthly Bill - {user[0]}")
    plt.xlabel("Months")
    plt.ylabel("Amount (₹)")
    plt.show()

# Insert new user + bills

def add_user():
    try:
        user_id = int(input("Enter new user ID: "))
        name = input("Enter user name: ")

        cursor.execute("INSERT INTO users VALUES (?, ?)", (user_id, name))

        for month in months_list:
            amount = int(input(f"Enter bill for {month}: "))
            cursor.execute("INSERT INTO bills VALUES (?, ?, ?)", (user_id, month, amount))

        conn.commit()
        print("User added successfully!")

    except Exception as e:
        print("Error:", e)

# Menu

while True:
    print("\n1. View User Bill")
    print("2. Add New User")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            uid = int(input("Enter User ID between 1 to 20: "))
            fetch_user(uid)
        except:
            print("Invalid input")

    elif choice == "2":
        add_user()

    elif choice == "0":
        break

    else:
        print("Invalid choice")

conn.close()