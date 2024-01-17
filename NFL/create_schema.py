import psycopg2
import urllib.parse as urlparse
import os

# Assume your database URL is stored in an environment variable
database_url = os.environ['DATABASE_URL']

# Parse the database URL
parsed_url = urlparse.urlparse(database_url)
dbname = parsed_url.path[1:]
user = parsed_url.username
password = parsed_url.password
host = parsed_url.hostname
port = parsed_url.port

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute("DROP SCHEMA IF EXISTS nfl CASCADE;")

# Create a schema
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

# Commit changes and close the cursor and connection
conn.commit()
cur.close()
conn.close()
