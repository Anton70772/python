import tkinter as tk
from tkinter.ttk import Treeview
import pymysql

connection_data = dict(
    username='root',
    password='234565',
    host="localhost",
    db='db77'
)

# Создаем окно
window = tk.Tk()
window.title("Результат запроса")

# Создаем объект Treeview для вывода результата
tree = Treeview(window, columns=("id", "name"))
tree.heading("#0", text="№")
tree.heading("id", text="ID")
tree.heading("name", text="Имя")
tree.pack()

# Устанавливаем соединение с базой данных
connection = pymysql.connect(
    host=connection_data['host'],
    user=connection_data['username'],
    passwd=connection_data['password'],
    db=connection_data['db']
)

# Если соединение установлено успешно, создаем курсор
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    # Добавляем строки в таблицу
    for row_num, row_data in enumerate(result, start=1):
        tree.insert("", "end", text=row_num, values=row_data)
    # Закрываем соединение
    connection.close()
else:
    tree.insert("", "end", text="Ошибка подключения к базе данных")

# Запускаем главный цикл окна
window.mainloop()
