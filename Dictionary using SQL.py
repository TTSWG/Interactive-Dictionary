import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word")
query = cursor.execute("SELECT * from Dictionary WHERE Expression = '%s' " %word)
result = cursor.fetchall()

if result:
    for r in result:
        print(r[1])
else:
    print("No word found")