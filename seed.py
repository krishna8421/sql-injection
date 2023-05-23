import sqlite3

def seed_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       email TEXT,
                       password TEXT)''')

    # Check if the default user already exists
    cursor.execute("SELECT * FROM users WHERE email=?", ('admin@example.com',))
    data = cursor.fetchone()

    if data is None:
        # Seed the database with a default user
        default_email = 'admin@example.com'
        default_password = 'password'

        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                       (default_email, default_password))

        conn.commit()

    conn.close()

# Call the seed_database function to seed the database
seed_database()
