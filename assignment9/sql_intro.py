
import sqlite3
# Function to add a publisher
def add_publisher(conn, name):
    try:
        conn.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
            (name,)
        )

        cursor = conn.execute(
            "SELECT id FROM publishers WHERE name = ?",
            (name,)
        )

        return cursor.fetchone()[0]

    except sqlite3.Error as error:
        print("Error adding publisher:", error)
        return None

# Function to add a magazine
def add_magazine(conn, name, publisher_id):
    try:
        conn.execute(
            """
            INSERT OR IGNORE INTO magazines (name, publisher_id)
            VALUES (?, ?)
            """,
            (name, publisher_id)
        )
        cursor = conn.execute(
             "SELECT id FROM magazines WHERE name = ?", 
            (name,)
         ) 
        return cursor.fetchone()[0]
    
    except sqlite3.Error as error:
        print("Error adding magazine:", error)
        return None

# Function to add a subscriber
def add_subscriber(conn, name, address):
    try:
        cursor = conn.execute(
            """
            SELECT id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )
        row = cursor.fetchone()

        if row is not None:
            return row[0]

        cursor = conn.execute(
                """
                INSERT INTO subscribers (name, address)
                VALUES (?, ?)
                """,
                (name, address)
            )
        return cursor.lastrowid
    
    except sqlite3.Error as error:
        print("Error adding subscriber:", error)
        return None

# Function to add a subscription
def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        cursor = conn.execute(
            """
            SELECT subscriber_id
            FROM subscriptions
            WHERE subscriber_id = ? AND magazine_id = ?
            """,
            (subscriber_id, magazine_id)
        )

        if cursor.fetchone() is None:
            conn.execute(
                """
                INSERT INTO subscriptions
                (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
                """,
                (subscriber_id, magazine_id, expiration_date)
            )

    except sqlite3.Error as error:
        print("Error adding subscription:", error)

try:
    # Connect to the database
    conn = sqlite3.connect("../db/magazines.db")

    # Enable foreign key checking
    conn.execute("PRAGMA foreign_keys = 1")

    # Create publishers table
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        )
        """
    )

    # Create magazines table
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        )
        """
    )

    # Create subscribers table
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """
    )

    # Create subscriptions table
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id),
            UNIQUE (subscriber_id,magazine_id)
        )
        """
    )

    # Add publishers and get their actual IDs
    publisher1 = add_publisher(conn, "Penguin Random House")
    publisher2 = add_publisher(conn, "Condé Nast")
    publisher3 = add_publisher(conn, "Hearst")

    # Add magazines using the actual publisher IDs
    magazine1 = add_magazine(conn, "The New Yorker", publisher2)
    magazine2 = add_magazine(conn, "National Geographic", publisher3)
    magazine3 = add_magazine(conn, "Vogue", publisher2)

    
    # Add subscribers and get their actual IDs
    subscriber1 = add_subscriber(conn, "John Smith", "123 Main Street")
    subscriber2 = add_subscriber(conn, "Mary Johnson", "456 Oak Avenue")
    subscriber3 = add_subscriber(conn, "John Smith", "789 Pine Road")

    #Add subscriptions using the actual subscriber and magazine IDs
    add_subscription(conn, subscriber1, magazine1, "2027-09-01")
    add_subscription(conn, subscriber2, magazine2, "2027-10-15")
    add_subscription(conn, subscriber3, magazine3, "2027-12-31")
    # Save changes
    conn.commit()
    
    #Task 4:Retrieve all subscribers
    print("\nAll subscribers:")
    cursor = conn.execute("SELECT * FROM subscribers")

    for row in cursor:
        print(row)

    #Retrieve all magazines sorted by name
    print("\n All  magazines sorted by name ")
    cursor = conn.execute(
        "SELECT * FROM magazines ORDER BY name")

    for row in cursor:
        print(row)

    #Find magazines for a particular publisher
    print ("\nAll magazines for a particular publisher ")
    cursor = conn.execute(
    """
    SELECT magazines.name
    FROM magazines
    JOIN publishers
    ON magazines.publisher_id = publishers.id
    WHERE publishers.name = ?
    """,
    ("Condé Nast",)
    )
 
    for row in cursor:
        print(row) 

    print("Tables created and data added successfully!")

except sqlite3.Error as error:
    print("Error:", error)

finally:
    if "conn" in locals():
        conn.close()
        print("Database connection closed.")

