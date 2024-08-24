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
        phoneNumber TEXT NOT NULL UNIQUE
    )
    ''')



    conn.commit()
    conn.close()


def addUsers():
    conn = sqlite3.connect('dorm_security.db')
    cursor = conn.cursor()

    data = [
        ("890000000", "Johnny", "2253059053"),
        ("890000001", "Jane", "2255555556"),
        ("890000002", "John", "2255555557"),
        ("890000003", "Janet", "2255555558"),
        ("890000004", "John", "2255555559"),
        ("890000005", "Janet", "2254445558")
    ]

    cursor.executemany("INSERT INTO Users (lsuId, name, phoneNumber) VALUES (?, ?, ?)", data)
    conn.commit()

def addDormMembers():
    conn = sqlite3.connect('dorm_security.db')
    cursor = conn.cursor()

    data = [
        ("890000000", "2253059053", "1234"),
        ("890000000", "2253019053", "1234"),
        ("890000000", "2253029053", "4312"),
        ("890000003", "2253049053", "1223"),
        ("890000004", "2255555555", "4321"),
        ("890000005", "2255555556", "1234"),
    ]

    cursor.executemany("INSERT INTO DormMembers (lsuId, name, phoneNumber, pin) VALUES (?, ?, ?, ?)", data)
    conn.commit()


# create_database()
# addUsers()