import sqlite3

conn = sqlite3.connect("People.db")

curser = conn.cursor() #allow us to write statements

curser.execute("""DROP TABLE IF EXISTS people;""")

curser.execute("""CREATE TABLE people (
name VARCHAR(255) NOT NULL,
job VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
age INT);""")

#put in some values
curser.execute("""INSERT INTO people (name,job,password,age) VALUES
("Mookie", "Programmer", "notNull", 29),
("Symba", "Hunter", "mainecoon", 25),
("Inky", "Marketing", "Kats", 27),
("Tom", "UX Designer", "prawns", 26);""")
conn.commit()

###
"""By entering 50 OR 1=1 we get all the results! Not good :("""

# print("First try an age. Second re-run the program and try '50 or 1=1'")
# age = input("Enter an age: ") #interacts with the database...
#
# curser.execute(f"SELECT * FROM people WHERE age > {age}")
# rows = curser.fetchall()
# for row in rows:
#     print(row)


# ---------------------------------------- #
# ---------------------------------------- #

"""
Login issues - strings can be changed to manipulate the structure of the query --> such as a condition that is always true! 1=1
Extra quotations, single quotes, can be added to provide an empty string and an additional one to add the OR logical statement.
String concatenation or formatted strings are used here.
"""
name_input = input("Enter username: ")
password_input = input("Enter a password: ")

curser.execute(f"SELECT * FROM people WHERE name = '{name_input}' AND password = '{password_input}'")
                                                                                #^ First quote ' OR '1' = '1   ^last quote mark
rows = curser.fetchall()

if len(rows) == 0:
    print("Login Failure")
else:
    print(f"Success! Here is the information of {name_input}")
    for row in rows:
        print(row)

# ---------------------------------------- #
# ---------------------------------------- #

"""Fixing it - Use of prepared statements"""
print("\nTry again...")

name_input2 = input("Enter username: ")
password_input2 = input("Enter a password: ")

#similar to above but place holders (?) are used to accept a value, not string. Then tuple for fstring.
curser.execute(f"SELECT * FROM people WHERE name = ? AND password = ?", (name_input2,password_input2))
rows = curser.fetchall()

if len(rows) == 0:
    print("Login Failure")
else:
    print(f"Success! Here is the information of {name_input}")
    for row in rows:
        print(row)
