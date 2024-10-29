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
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')
    connection.commit()


def fill_db(idx, title, description, price):
    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?,?,?,?)',
                   (f'{idx}', f'{title}', f'{description}', f'{price}'))
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    prod_list = cursor.fetchall()
    connection.commit()
    return prod_list


def add_user(username, email, age, balance=1000):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (f'{username}', f'{email}', f'{age}', f'{balance}'))
    connection.commit()


def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True


initiate_db()
for i in range(1, 5):
    fill_db(f'{i}', 'Яблоки', f'{i} штук(а/и)', f'{i * 100}')

pprint(get_all_products())

connection.commit()
# connection.close()
