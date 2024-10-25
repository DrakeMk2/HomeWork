import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
''')

cursor.execute('''DELETE FROM Users''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

cursor.execute('SELECT * FROM Users WHERE age != 60')
for i in cursor.fetchall():
    print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
usr_cnt = cursor.fetchone()[0]


cursor.execute('SELECT SUM(balance) FROM Users')
sum_bal = cursor.fetchone()[0]
print(f'Cредний баланс всех пользователей: {sum_bal/usr_cnt}')

cursor.execute('SELECT AVG(balance) FROM Users')
avg_bal = cursor.fetchone()[0]
print(f'Тоже средний баланс пользователей: {avg_bal}')

for i in cursor.fetchall():
    print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

connection.commit()
connection.close()
