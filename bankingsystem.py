# Banking Management System

import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    acc_no INTEGER PRIMARY KEY,
    name TEXT,
    balance INTEGER
)
""")

# Insert sample accounts (only once)
accounts = [(i, f"User_{i}", 10000) for i in range(1001, 1021)]
cursor.executemany("INSERT OR IGNORE INTO accounts VALUES (?, ?, ?)", accounts)
conn.commit()

# Functions

def view_account(acc_no):
    cursor.execute("SELECT * FROM accounts WHERE acc_no=?", (acc_no,))
    acc = cursor.fetchone()

    if acc:
        print(f"\nAccount No: {acc[0]}")
        print(f"Name: {acc[1]}")
        print(f"Balance: ₹{acc[2]}")
    else:
        print("Account not found")


def deposit(acc_no, amount):
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?", (amount, acc_no))
    conn.commit()
    print("Amount deposited")


def withdraw(acc_no, amount):
    cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc_no,))
    result = cursor.fetchone()

    if result and result[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?", (amount, acc_no))
        conn.commit()
        print("Amount withdrawn")
    else:
        print("Insufficient balance or account not found")


def create_account():
    try:
        acc_no = int(input("Enter account number: "))
        name = input("Enter name: ")
        balance = int(input("Enter initial balance: "))

        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)", (acc_no, name, balance))
        conn.commit()
        print("Account created successfully")

    except Exception as e:
        print("Error:", e)

# Menu

while True:
    print("\n1. View Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Create Account")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = int(input("Enter account number: "))
        view_account(acc_no)

    elif choice == "2":
        acc_no = int(input("Enter account number: "))
        amount = int(input("Enter amount: "))
        deposit(acc_no, amount)

    elif choice == "3":
        acc_no = int(input("Enter account number: "))
        amount = int(input("Enter amount: "))
        withdraw(acc_no, amount)

    elif choice == "4":
        create_account()

    elif choice == "0":
        break

    else:
        print("Invalid choice")

conn.close()
