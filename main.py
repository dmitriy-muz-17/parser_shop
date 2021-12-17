import parser
import sqlite3


def insert_data_to_db():
    db = sqlite3.connect('archive.db')
    sql = db.cursor()
    #sql.execute("DROP TABLE cars")
    #db.commit()
    sql.execute("""CREATE TABLE IF NOT EXISTS cars (
        name TEXT,
        url TEXT,
        price TEXT,
        price_uah TEXT
    )""")
    db.commit()
    e_cars = parser.parse()
    for i in e_cars:
        sql.execute(f"INSERT INTO cars VALUES (?, ?, ?, ?)", (i['name'], i['link'], i['price_usd'], i['price_uah']))
        db.commit()
    for value in sql.execute("SELECT * FROM cars"):
        print(value)


insert_data_to_db()
