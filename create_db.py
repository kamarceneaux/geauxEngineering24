import sqlite3

# File used to create the database

def create_database():
    conn = sqlite3.connect('dorm_security.db')
    cursor = conn.cursor()

    # Create User table
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS DormMembers (
    #     lsuId TEXT PRIMARY KEY,
    #     pin TEXT NOT NULL,
    #     dormNumber TEXT,
    #     FOREIGN KEY (dormNumber) REFERENCES Dorm(dormNumber)
    # )
    # ''')

    # Create Dorm table
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS Dorm (
    #     dormNumber TEXT PRIMARY KEY,
    #     lsuId TEXT UNIQUE,
    #     FOREIGN KEY (lsuId) REFERENCES User(lsuId)
    # )
    # ''')

    # Create User table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        lsuId TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        securityQuestion TEXT NOT NULL UNIQUE,
        securityAnswer TEXT NOT NULL
    )
    ''')



    conn.commit()
    conn.close()


def addUsers():
    conn = sqlite3.connect('dorm_security.db')
    cursor = conn.cursor()

    data = [
        ("890000000", "John Doe", "What is your favorite color?", "Blue"),
        ("890000001", "Jane Doe", "What is your favorite animal?", "Dog"),
        ("890000002", "John Smith", "What is your favorite food?", "Pizza"),
        ("890000003", "Jane Smith", "What is your favorite movie?", "Inception"),
        ("890000004", "John Johnson", "What is your favorite book?", "Harry Potter"),
        ("890000005", "Jane Johnson", "What is your favorite song?", "Bohemian Rhapsody")
    ]

    cursor.executemany("INSERT INTO Users (lsuId, name, securityQuestion,securityAnswer  ) VALUES (?, ?, ?, ?)", data)
    conn.commit()

def addDormMembers():
    conn = sqlite3.connect('dorm_security.db')
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO DormMembers (lsuId, name, phoneNumber, pin) VALUES (?, ?, ?, ?)", data)
    conn.commit()


create_database()
addUsers()