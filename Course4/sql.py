import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS Ages')
cursor.execute('CREATE TABLE Ages (id INTEGER PRIMARY KEY, name VARCHAR(128), age INTEGER)')

users=[
    ('Kellsie', 27),
    ('Aniqa', 40),
    ('Elyssa', 39),
    ('Aibidh', 13),
    ('Caley', 39)
]

for name, age in users:
    cursor.execute("INSERT OR REPLACE INTO Ages (name, age) VALUES (?, ?)", (name, age))
    
connection.commit()

final = cursor.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X").fetchall()


connection.close()

print("Database and table created successfully.")
for fila in final:
    print(fila[0])
