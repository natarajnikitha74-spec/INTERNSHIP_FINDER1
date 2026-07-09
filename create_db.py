import sqlite3

conn=sqlite3.connect("database.db")

c=conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS internships(
id INTEGER PRIMARY KEY AUTOINCREMENT,
company TEXT,
role TEXT,
location TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS applications(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
internship_id INTEGER
)
""")

c.execute("INSERT INTO internships(company,role,location) VALUES('Google','Python Intern','Bangalore')")
c.execute("INSERT INTO internships(company,role,location) VALUES('Microsoft','AI Intern','Hyderabad')")
c.execute("INSERT INTO internships(company,role,location) VALUES('Amazon','Web Developer','Chennai')")

conn.commit()
conn.close()

print("Database Created")