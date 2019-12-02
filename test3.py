import sqlite3
import datetime

conn = sqlite3.connect('BotSwearing.db')
cursor = conn.cursor()

date = datetime.datetime.today()
date2 = date.strftime("%Y.%m.%d")

cursor.execute("SELECT * FROM Swearings")
results = cursor.fetchall()
for result in results:
    if result[1] == date2:
        number = result[0]
        number2 = result[2] + 1
        cursor.execute("UPDATE Swearings SET Count = " + str(number2) + " WHERE ID = " + str(number))
        conn.commit()

print(results)
print(results[0])
print(type(results[0][1]))

#cursor.execute("INSERT INTO Swearings(Date, Count) VALUES ('2019.12.02', '100')")
#conn.commit()

#cursor.execute("SELECT * FROM Swearings WHERE date = '" + date2 + "' GROUP BY Date")
#results = cursor.fetchall()
#print(results)

#cursor.execute("SELECT SUM(Count) FROM Swearings WHERE date = '" + date2 + "'")
#results = cursor.fetchall()
#print(results)  

conn.close()