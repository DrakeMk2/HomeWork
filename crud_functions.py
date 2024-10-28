import sqlite3
from pprint import pprint

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    
    )
    ''')
    cursor.execute('''DELETE FROM Products''')


def fill_db(idx, title, description, price):
    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?,?,?,?)',
                   (f'{idx}', f'{title}', f'{description}', f'{price}'))


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    prod_list = cursor.fetchall()
    return prod_list


initiate_db()
for i in range(1, 5):
    fill_db(f'{i}', 'Яблоки', f'{i} штук(а/и)', f'{i * 100}')

pprint(get_all_products())

connection.commit()
# connection.close()
