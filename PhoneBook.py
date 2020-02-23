import sqlite3
conn = sqlite3.connect("pb.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Contacts
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    'name' TEXT,
                                    'surname' TEXT ,
                                    'phone' INTEGER)''')


conn.execute('insert into Contacts ( name, surname, phone) values( "Evgeniy", "Stupka", +380501112211)')
conn.execute('insert into Contacts ( name, surname, phone) values( "Aleksandr", "Gunko", +380507777777)')
conn.execute('insert into Contacts ( name, surname, phone) values( "Victor", "Matat", +380502221122)')
conn.commit()