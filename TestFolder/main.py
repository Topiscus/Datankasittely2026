import sqlite3
query = """ CREATE TABLE test (a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER ); """
con = sqlite3.connect("mydata.sqlite")
con.execute(query)
con.commit()

data = [
  ("Atlanta", "Georgia", 1.25, 6),
  ("Tallahassee", "Florida", 2.6, 3),
  ("Sacramento", "California", 1.7, 5)
]

stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()
