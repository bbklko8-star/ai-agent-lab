import sqlite3

conn = sqlite3.connect("database/questions.db")
cursor = conn.cursor()

cursor.execute("SELECT question, option_a, option_b, option_c, option_d FROM questions")

rows = cursor.fetchall()

for r in rows:
    print("\nQuestion:", r[0])
    print("A:", r[1])
    print("B:", r[2])
    print("C:", r[3])
    print("D:", r[4])

conn.close()