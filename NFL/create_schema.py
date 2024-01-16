import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="docker",
    password="docker"
)

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("DROP SCHEMA IF EXISTS nfl CASCADE;")

#Create a schema
cur.execute("CREATE SCHEMA IF NOT EXISTS nfl;")

# Create a Users table
cur.execute("""
    CREATE TABLE IF NOT EXISTS nfl.users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        number VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL
    );
""")

# Create an Entries table
cur.execute("""
    CREATE TABLE IF NOT EXISTS nfl.entries (
        id SERIAL PRIMARY KEY,
        home_team VARCHAR(255) NOT NULL,
        selected_option VARCHAR(255) NOT NULL,
        away_team VARCHAR(255) NOT NULL,
        user_id INTEGER REFERENCES nfl.Users (id)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS nfl.entries (
        id SERIAL PRIMARY KEY,
        home_team VARCHAR(255) NOT NULL,
        selected_option VARCHAR(255) NOT NULL,
        away_team VARCHAR(255) NOT NULL,
        user_id INTEGER REFERENCES nfl.Users (id)
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS nfl.entries (
        id SERIAL PRIMARY KEY,
        home_team VARCHAR(255) NOT NULL,
        selected_option VARCHAR(255) NOT NULL,
        away_team VARCHAR(255) NOT NULL,
        user_id INTEGER REFERENCES nfl.Users (id)
    );
""")

#Commit changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
