import sqlite3

connection = sqlite3.connect("outputs/day_27_transactions.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS accounts")

cursor.execute("""
CREATE TABLE accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL CHECK(balance >= 0)
)
""")

accounts = [
    ("An", 1000),
    ("Binh", 500),
    ("Chi", 700)
]

cursor.executemany("""
INSERT INTO accounts (name, balance)
VALUES (?, ?)
""", accounts)

connection.commit()

print("Initial accounts:")

cursor.execute("""
SELECT *
FROM accounts
""")

for row in cursor.fetchall():
    print(row)

print()

try:
    cursor.execute("""
    UPDATE accounts
    SET balance = balance - ?
    WHERE name = ?
    """, (200, "An"))

    cursor.execute("""
    UPDATE accounts
    SET balance = balance + ?
    WHERE name = ?
    """, (200, "Binh"))

    connection.commit()

    print("Transfer successful!")

except sqlite3.Error as error:
    connection.rollback()
    print("Transaction failed:", error)


print("After transfer:")

cursor.execute("""
SELECT *
FROM accounts
""")

for row in cursor.fetchall():
    print(row)

print()

try:
    cursor.execute("""
    UPDATE accounts
    SET balance = balance - ?
    WHERE name = ?
    """, (100, "An"))

    cursor.execute("""
    UPDATE wrong_table
    SET balance = balance + ?
    WHERE name = ?
    """, (100, "Chi"))

    connection.commit()

except sqlite3.Error as error:
    connection.rollback()

    print("Transaction rolled back:", error)


def transfer_money(connection, cursor, sender, receiver, amount):

    if amount <= 0:
        print("Invalid amount")
        return

    # kiểm tra sender
    cursor.execute("""
    SELECT balance
    FROM accounts
    WHERE name = ?
    """, (sender,))

    sender_row = cursor.fetchone()

    if sender_row is None:
        print("Invalid sender")
        return

    balance = sender_row[0]

    # kiểm tra receiver
    cursor.execute("""
    SELECT id
    FROM accounts
    WHERE name = ?
    """, (receiver,))

    receiver_row = cursor.fetchone()

    if receiver_row is None:
        print("Invalid receiver")
        return

    # không cho chuyển cho chính mình
    if sender == receiver:
        print("Sender and receiver cannot be the same")
        return

    # kiểm tra số dư
    if balance < amount:
        print("Not enough balance")
        return

    # transaction
    try:
        cursor.execute("""
        UPDATE accounts
        SET balance = balance - ?
        WHERE name = ?
        """, (amount, sender))

        cursor.execute("""
        UPDATE accounts
        SET balance = balance + ?
        WHERE name = ?
        """, (amount, receiver))

        connection.commit()

        print("Transfer successful")

    except sqlite3.Error as error:
        connection.rollback()
        print("Transaction failed:", error)


print("\nTest 1: Valid transfer")
transfer_money(connection, cursor, "An", "Binh", 100)

print("\nTest 2: Not enough balance")
transfer_money(connection, cursor, "An", "Chi", 5000)

print("\nTest 3: Invalid sender")
transfer_money(connection, cursor, "ABC", "Chi", 100)

print("\nTest 4: Invalid receiver")
transfer_money(connection, cursor, "An", "XYZ", 100)

print("\nTest 5: Invalid amount")
transfer_money(connection, cursor, "An", "Chi", -100)

print("\nFinal accounts:")

cursor.execute("""
SELECT *
FROM accounts
""")

for row in cursor.fetchall():
    print(row)

connection.close()