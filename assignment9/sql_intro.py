
import sqlite3


# Function to add a publisher
def add_publisher(conn, name):
    try:
        conn.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
            (name,)
        )
    except sqlite3.Error as error:
        print("Error adding publisher:", error)


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
    except sqlite3.Error as error:
        print("Error adding magazine:", error)


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

        if cursor.fetchone() is None:
            conn.execute(
                """
                INSERT INTO subscribers (name, address)
                VALUES (?, ?)
                """,
                (name, address)
            )

    except sqlite3.Error as error:
        print("Error adding subscriber:", error)


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
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        )
        """
    )

    # Add publishers
    add_publisher(conn, "Penguin Random House")
    add_publisher(conn, "Condé Nast")
    add_publisher(conn, "Hearst")

    # Add magazines
    add_magazine(conn, "The New Yorker", 2)
    add_magazine(conn, "National Geographic", 3)
    add_magazine(conn, "Vogue", 2)

    # Add subscribers
    add_subscriber(conn, "John Smith", "123 Main Street")
    add_subscriber(conn, "Mary Johnson", "456 Oak Avenue")
    add_subscriber(conn, "John Smith", "789 Pine Road")

    # Add subscriptions
    add_subscription(conn, 1, 1, "2027-09-01")
    add_subscription(conn, 2, 2, "2027-10-15")
    add_subscription(conn, 3, 3, "2027-12-31")

    # Save changes
    conn.commit()
    
    #Task 4:Retrieve all subscribers
    print("\nAll subscribers:")
    cursor = conn.execute("SELECT * FROM subscribers")

    for row in cursor:
        print(row)

    #Retrieve all magazines sorted by name
    print("\n All  magazines sorted by name ")
    cursor = conn.execute("SELECT * FROM magazines ORDER BY name")

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

