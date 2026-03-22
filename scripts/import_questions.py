import pandas as pd
import sqlite3


# Load CSV file
df = pd.read_csv("data/questions.csv")

# Connect to SQLite database
conn = sqlite3.connect("database/questions.db")

# Save data
df.to_sql("questions", conn, if_exists="replace", index=False)

conn.close()

print("Questions imported successfully!")
