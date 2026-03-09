import sqlite3

conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

# cursor.execute ("""
# CREATE TABLE utilisateurs (
# id INTEGER PRIMARY KEY ,
# nom TEXT ,
# age INTEGER
# )
# """)
# conn . commit ()

# cursor . execute (
# " INSERT INTO utilisateurs ( nom , age ) VALUES (? , ?) " ,
# ( " Alice " , 25 )
# )
# conn . commit ()

# donnees = [
#     ("Bob",30),
#     ("Charlie",22),
#     ("Diane",28)
# ]

# cursor . executemany (
# " INSERT INTO utilisateurs ( nom , age ) VALUES (? , ?) " ,
# donnees
# )

# conn . commit ()

# cursor . execute ( " SELECT * FROM utilisateurs " )
# resultats = cursor . fetchall ()

# for ligne in resultats :
#     print ( ligne )

cursor . execute (
" SELECT nom FROM utilisateurs WHERE age > ? " ,
(25 ,)
)
for ligne in cursor . fetchall () :
    print ( ligne )
conn . close ()