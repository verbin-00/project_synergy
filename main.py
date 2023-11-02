import tkinter as tk        # Импортировали библиотеку tkinter
from tkinter import ttk     # Из библиотеки tkinter импортируем ttk
import sqlite3              # Импортируем  библиотеку sqlite3


class Main(tk.Frame):                                       # Класс главного окна
    def __init__(self, root):                               # Конструктор класса
        super().__init__(root)                              # Даём наследование всех свойств класса tkinter, функций и методов  
        self.init_main()                                    # Вызываем метод init_main
        self.db = db                                        # Объявляем переменную в классе
        self.view_records()                                 # Вызываем метод view_records

    def init_main(self):                                    # Метод хранения и инициализация обЪектов GUI
                                                            # Создаём панель инструментов toolbar
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)              # Frame - виджет для формирования и скрепления других виджетов в окне приложения
                                                            # Устанавливаем цвет фона (bg) и границу (bd)
        toolbar.pack(side=tk.TOP, fill=tk.X)                # Закрепляем сверху (side) и расстягиваем по горизонтали X (fill)

        # Добавляем Treeview и создаём таблицу с колонками (columns):"ID", "name", "tel", "email","salary". Задаём высоту таблицы (height) и скрываем пустую(нулевую) колонку таблицы (show)
        self.tree = ttk.Treeview(
            self, columns=("ID", "name", "tel", "email","salary"), height=45, show="headings"
        )

        self.tree.column("ID", width=30, anchor=tk.CENTER)          # Указываем параметры колонки("ID"), задаём ширину (width) и выравниваем по центру (anchor=tk.CENTER)
        self.tree.column("name", width=300, anchor=tk.CENTER)       # Указываем параметры колонки("name"), задаём ширину (width) и выравниваем по центру (anchor=tk.CENTER)
        self.tree.column("tel", width=150, anchor=tk.CENTER)        # Указываем параметры колонки("tel"), задаём ширину (width) и выравниваем по центру (anchor=tk.CENTER)
        self.tree.column("email", width=150, anchor=tk.CENTER)      # Указываем параметры колонки("email"), задаём ширину (width) и выравниваем по центру (anchor=tk.CENTER)
        self.tree.column("salary", width=90, anchor=tk.CENTER)      # Указываем параметры колонки("salary"), задаём ширину (width) и выравниваем по центру (anchor=tk.CENTER)

        self.tree.heading("ID", text="ID")                          # Задаём название заголовка для "ID" и указываем, как должно отображаться название колонки (text)
        self.tree.heading("name", text="ФИО")                       # Задаём название заголовка для "name" и указываем, как должно отображаться название колонки (text)
        self.tree.heading("tel", text="Телефон")                    # Задаём название заголовка для "tel" и указываем, как должно отображаться название колонки (text)
        self.tree.heading("email", text="E-mail")                   # Задаём название заголовка для "email" и указываем, как должно отображаться название колонки (text)
        self.tree.heading("salary", text="Зарплата")                # Задаём название заголовка для "salary" и указываем, как должно отображаться название колонки (text)

        self.tree.pack(side=tk.LEFT)                                # Размещение кнопки в окне (*.pack) и выравнивание по левому краю (side=tk.LEFT)

        self.add_img = tk.PhotoImage(file="./img/add.png")          # Создали кнопку добавления и загрузили её изображение 
        
        btn_open_dialog = tk.Button(
            toolbar, bg="#d7d8e0", bd=0, image=self.add_img, command=self.open_dialog
        )
        # 1 - Привязываем к панели инструментов (toolbar)
        # 2 - Установливаем цвет фона (bg)
        # 3 - Установливаем размер (bd)
        # 4 - Установливаем иконку (image)
        # 5 - Устанавливаем функцию, которая сработает при нажатии на кнопку (command)
        btn_open_dialog.pack(side=tk.LEFT)                          # Размещение кнопки в окне (*.pack) и выравнивание по левому краю (side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="./img/update.png")    # Создали кнопку изменения данных и загрузили её изображение
        
        btn_edit_dialog = tk.Button(
            toolbar,
            bg="#d7d8e0",
            bd=0,
            image=self.update_img,
            command=self.open_update_dialog,
        )
        # Создали кнопку
        # 1 - Привязываем к панели инструментов (toolbar)
        # 2 - Установливаем цвет фона (bg)
        # 3 - Установливаем размер (bd)
        # 4 - Установливаем иконку (image)
        # 5 - Устанавливаем функцию, которая сработает при нажатии на кнопку (command)
        btn_edit_dialog.pack(side=tk.LEFT)                          # Размещение кнопки в окне (*.pack) и выравнивание по левому краю (side=tk.LEFT)


        self.delete_img = tk.PhotoImage(file="./img/delete.png")    # Создали кнопку удаления и загрузили её изображение
        btn_delete = tk.Button(
            toolbar,
            bg="#d7d8e0",
            bd=0,
            image=self.delete_img,
            command=self.delete_records,
        )
        # 1 - Привязываем к панели инструментов (toolbar)
        # 2 - Установливаем цвет фона (bg)
        # 3 - Установливаем размер (bd)
        # 4 - Установливаем иконку (image)
        # 5 - Устанавливаем функцию, которая сработает при нажатии на кнопку (command)        
        btn_delete.pack(side=tk.LEFT)                               # Размещение кнопки в окне (*.pack) и выравнивание по левому краю (side=tk.LEFT)


        self.search_img = tk.PhotoImage(file="./img/search.png")    # Создали кнопку поиска и загрузили её изображение
        btn_search = tk.Button(
            toolbar,
            bg="#d7d8e0",
            bd=0,
            image=self.search_img,
            command=self.open_search_dialog,
        )
        # 1 - Привязываем к панели инструментов (toolbar)
        # 2 - Установливаем цвет фона (bg)
        # 3 - Установливаем размер (bd)
        # 4 - Установливаем иконку (image)
        # 5 - Устанавливаем функцию, которая сработает при нажатии на кнопку (command)
        btn_search.pack(side=tk.LEFT)                                 # Размещение кнопки в окне (*.pack) и выравнивание по левому краю (side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="./img/refresh.png")    # Создали кнопку обновления и загрузили её изображение
        btn_refresh = tk.Button(
            toolbar,
            bg="#d7d8e0",
            bd=0,
            image=self.refresh_img,
            command=self.view_records,
        )
        # 1 - Привязываем к панели инструментов (toolbar)
        # 2 - Установливаем цвет фона (bg)
        # 3 - Установливаем размер (bd)
        # 4 - Установливаем иконку (image)
        # 5 - Устанавливаем функцию, которая сработает при нажатии на кнопку (command)
        btn_refresh.pack(side=tk.LEFT)                                 # Размещение кнопки в окне (*.pack) и выравнивание по левому краю (side=tk.LEFT)  

    def open_dialog(self):                                                              # Метод отвечающий за вызов дочернего окна
        Child()                                                                         # Вызвали класс, который отвечает за добавление данных в базу данных

    def records(self, name, tel, email,salary ):                                        # Метод добавления данных
        self.db.insert_data(name, tel, email,salary )                                   # Вызвали функцию, которая отвечает за добавление данных в базу данных
        self.view_records()                                                             # Вызвали функцию, которая отвечает за обновление данных и вывод данных на экран

    def view_records(self):                                                             # Метод выводящий данные в таблицу
        self.db.cursor.execute("SELECT * FROM Employees")                               # Выбираем данные из таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]                         # Удаляем старые данные
        [self.tree.insert("", "end", values=row) for row in self.db.cursor.fetchall()]  # Вписываем новые данные в базу данных

    def open_update_dialog(self):                                                       # Метод отвечающий за вызов окна для изменения данных в базе данных
        Update()                                                                        # Вызываем класс, который отвечает за изменение данных в базе данных

    def update_records(self, name, tel, email, salary):                                 # Метод обновления (изменения) данных
        self.db.cursor.execute(                                                         # Запрос на обновление данных
            """UPDATE Employees SET name=?, tel=?, email=?, salary=? WHERE id=?""",

            # Передаём аргуметы на места "?"
            (name, tel, email,salary, self.tree.set(self.tree.selection()[0], "#1")),
        )
        self.db.conn.commit()                                                           # Сохраняем запрос на обновление данных
        self.view_records()                                                             # Вызываем метод выводящий данные в таблицу

    def delete_records(self):                                                           # Метод удаления данных из базы данных
        for selection_items in self.tree.selection():
            self.db.cursor.execute(                                                     # Запрос на удаление строки из базы данных
                "DELETE FROM Employees WHERE id=?", (self.tree.set(selection_items, "#1"))     # Передаём аргумет на место "?"
            )
        self.db.conn.commit()                                                           # Сохраняем запрос на удаление строки из базы данных
        self.view_records()                                                             # Вызываем метод выводящий данные в таблицу

    def open_search_dialog(self):                                                       # Метод отвечающий за окно для поиска данных в базе данных
        Search()                                                                        # Вызываем класс, который отвечает за поиск данных в базе данных

    def search_records(self, name):                                                     # Метод отвечающий за поиск записи
        name = "%" + name + "%"                                                         # Добавляем к строчке знаки процента
        self.db.cursor.execute("SELECT * FROM Employees WHERE name LIKE ?", (name,))    # Передаем список name, а не просто name

        [self.tree.delete(i) for i in self.tree.get_children()]                         # Удаляем старые данные 
        [self.tree.insert("", "end", values=row) for row in self.db.cursor.fetchall()]  # Вписываем новые данные в базу данных


class Child(tk.Toplevel):                                   # Класс дочерних окон. Toplevel - окно верхнего уровня
    def __init__(self):                                     # Конструктор класса
        super().__init__(root)                              # Даём наследование всех свойств класса tkinter, функций и методов
        self.init_child()                                   # Вызов метода init_child
        self.view = app                                     # Объявляем переменную в классе

    def init_child(self):
        self.title("Добавить сотрудника")                   # Указываем заголовк окна (*.title)
        self.geometry("400x220")                            # Устанавливаем размер окна (*.geometry)
        self.resizable(False, False)                        # Устанавливаем ограничение изменения размеров окна (*.resizable)

        self.grab_set()                                     # Перехватываем весь пользовательский ввод
        self.focus_set()                                    # Устанавливаем фокус на нужном виджете, когда основное окно находится в фокусе.

        label_name = tk.Label(self, text="ФИО:")            # Создаём форму для ФИО 
        label_name.place(x=50, y=50)                        # Указываем координаты формы ФИО (*.place)
        label_select = tk.Label(self, text="Телефон:")      # Создаём форму для Телефона
        label_select.place(x=50, y=80)                      # Указываем координаты формы Телефона (*.place)
        label_sum = tk.Label(self, text="E-mail:")          # Создаём форму для E-mail
        label_sum.place(x=50, y=110)                        # Указываем координаты формы E-mail (*.place)
        label_salary = tk.Label(self, text="Зарплата:")     # Создание форму для Зарплаты
        label_salary.place(x=50, y=140)                     # Указываем координаты формы Зарплата (*.place)


        self.entry_name = ttk.Entry(self)                   # Создаём поле для ввода формы ФИО
        self.entry_name.place(x=200, y=50)                  # Указываем координаты поля для ввода формы ФИО (*.place)
        self.entry_email = ttk.Entry(self)                  # Создаём поле для ввода формы  E-mail
        self.entry_email.place(x=200, y=80)                 # Указываем координаты поля для ввода формы E-mail (*.place)
        self.entry_tel = ttk.Entry(self)                    # Создаём поле для ввода формы Телефон
        self.entry_tel.place(x=200, y=110)                  # Указываем координаты поля для ввода формы Телефон (*.place)
        self.entry_salary = ttk.Entry(self)                 # Создаём поле для ввода формы Зарплаты
        self.entry_salary.place(x=200, y=140)               # Указываем координаты поля для ввода формы Зарплата (*.place)

        # Создаём кнопку закрытия дочернего класса. Указываем текст на кнопке (text) и команду (command), которая выполниться при нажатии на кнопку
        # self.destroy - закрытие нынешнего окна
        # Указываем её координаты (*.place)
        self.btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        self.btn_cancel.place(x=220, y=170)

        # Создаём кнопку для добавления текста и указываем её координаты
        self.btn_ok = ttk.Button(self, text="Добавить")
        self.btn_ok.place(x=300, y=170)

        # Отслеживаем событие, при котором сработает кнопка ДОБАВИТЬ.
        # Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию records и передаём ей информацию из полей: name, email,tel
        self.btn_ok.bind(
            "<Button-1>",
            lambda event: self.view.records(
                self.entry_name.get(), self.entry_email.get(), self.entry_tel.get(), self.entry_salary.get()
            ),
        )


class Update(Child):                                                # Класс дочерних окон. Класс окна для обновления
    def __init__(self):                                             # Конструктор класса
        super().__init__()                                          # Даём наследование всех свойств класса tkinter, функций и методов
        self.init_edit()                                            # Вызываем метод init_edit
        self.view = app                                             # Объявляем переменную в классе
        self.db = db                                                # Объявляем переменную в класе
        self.default_data()                                         # Вызываем метод default_data


    def init_edit(self):                                            # Метод редактирования данных в базе данных
        self.title("Редактирование данных сотрудника")              # Указываем название заголовка (*.title)
        btn_edit = ttk.Button(self, text="Редактировать")           # Создаём кнопку и указываем текст на ней (text)
        btn_edit.place(x=205, y=170)                                # Указываем координаты кнопки (*.place)

        # Отслеживаем событие, при котором сработает кнопка ИЗМЕНИТЬ.
        # Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию update_records и передаём ей информацию из полей: name, email,tel
        btn_edit.bind(
            "<Button-1>",
            lambda event: self.view.update_records(
                self.entry_name.get(), self.entry_email.get(), self.entry_tel.get(), self.entry_salary.get()
            ),
        )

        # Отслеживаем событие, при котором сработает кнопка .
        # Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию destroy к самой кнопке
        # add='+'  - соединяем две функции bind этой кнопки
        btn_edit.bind(
            "<Button-1>",
            lambda event: self.destroy(), add="+"
        )

        self.btn_ok.destroy()                                               # Закрываем кнопку btn_ok

    def default_data(self):                                                 
        self.db.cursor.execute(                                             # Запрос на выбор всех полей с таким-то id
            "SELECT * FROM Employees WHERE id=?",
            self.view.tree.set(self.view.tree.selection()[0], "#1"),        # Выбираем id выделенной строки
        )
        row = self.db.cursor.fetchone()                         # Получаем первую запись
        self.entry_name.insert(0, row[1])                       # Передаём значение в поле из этой записи
        self.entry_email.insert(0, row[2])                      # Передаём значение в поле из этой записи
        self.entry_tel.insert(0, row[3])                        # Передаём значение в поле из этой записи
        self.entry_salary.insert(0,row[4])



class Search(tk.Toplevel):                                      # Класс дочерних окон. Класс окна поиска записи. Toplevel - окно верхнего уровня
    def __init__(self):                                         # Конструктор класса
        super().__init__()                                      # Даём наследование всех свойств класса tkinter, функций и методов
        self.init_search()                                      # Вызываем метод init_search
        self.view = app                                         # Объявляем переменную в классе

    def init_search(self):
        self.title("Поиск сотрудника")                          # Указываем название заголовка
        self.geometry("300x100")                                # Устанавливаем размер окна (*.geometry)
        self.resizable(False, False)                            # Устанавливаем ограничение изменения размеров окна (*.resizable)

        label_search = tk.Label(self, text="Имя:")              # Создаём форму для поиска ФИО
        label_search.place(x=50, y=20)                          # Указываем координаты формы для поиска по ФИО

        self.entry_search = ttk.Entry(self)                     # Создаём поле для ввода формы поиска по  ФИО
        self.entry_search.place(x=100, y=20, width=150)         # Указываем координаты поля для ввода формы поиска по  ФИО

        # Создаём кнопку и указываем текст на ней (text) и функцию (command), которая вызовется при нажатии на ней
        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)                           # Указываем координаты кнопки

        # Создаём кнопку и указываем текст на ней (text)
        search_btn = ttk.Button(self, text="Найти")
        search_btn.place(x=105, y=50)                           # Указываем координаты кнопки

        # Отслеживаем событие, при котором сработает кнопка ПОИСК.
        # Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию search_records и передаём ей информацию из поля entry_search
        search_btn.bind(
            "<Button-1>",
            lambda event: self.view.search_records(self.entry_search.get()),
        )
        # Отслеживаем событие, при котором сработает кнопка .
        # Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию destroy к самой кнопке
        search_btn.bind("<Button-1>", lambda event: self.destroy(), add="+")



class DB:                                                                               # Класс БД
    def __init__(self):                                                                 # Конструктор класса
        self.conn = sqlite3.connect("db.db")                                            # Создание соединения с базой данных(имя бд)
        self.cursor = self.conn.cursor()                                                # Вызываем курсор базы данных
        self.cursor.execute(                                                            # Запрос на создание базы данных
            '''
            CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            tel TEXT NOT NULL,
            email TEXT NOT NULL,
            salary INTEGER
            )
            '''
        )
        self.conn.commit()                                                              # Сохраняем запрос
        self.data()

    # Метод для добавления изначальных данных в базу данных
    def data(self):
        insert_into = 'INSERT INTO Employees (name, tel, email, salary) VALUES (?, ?, ?, ?)'


        user_data=('Evgeny Antonov', '+76534951682', 'evant@gmail.com','203604')
        user_data1=('Artem Volkov', '+31679465314', 'artvol@mail.ru','125400')
        user_data2=('Mark Kramber', '+11542351025', 'krabmark@yandex.com','100000')
        user_data3=('Max Nuts', '+49578613445', 'nutscool@email.com','116489')
        user_data4=('Jack Lion', '+25678135049', 'lionking@yahoo.com','95000')
        self.cursor.execute(insert_into,user_data )
        self.cursor.execute(insert_into,user_data1 )
        self.cursor.execute(insert_into,user_data2 )
        self.cursor.execute(insert_into,user_data3 )
        self.cursor.execute(insert_into,user_data4 )

        self.conn.commit()                                                                                          # Сохраняем запрос


    def insert_data(self, name, tel, email, salary):                                                                # Метод для добавления наших данных в таблицу
        self.cursor.execute(                                                                                        # Запрос на создание базы данных
            """INSERT INTO Employees(name, tel, email, salary) VALUES(?, ?, ?, ?)""", (name, tel, email, salary)    # передаём аргументы на места '?'
        )
        self.conn.commit()                                                                                          # Сохраняем запрос

if __name__ == "__main__":
    root = tk.Tk()                                  # Сохраняем экземпляр tkinter (root)
    db = DB()                                       # Создаём экземпляр класса с базой данных (db)
    app = Main(root)                                # Передаём экземпляр tkinter в класс Main (app)
    app.pack()                                      # Размещаем app в окне (*.pack)
    root.title("Список сотрудников компании")       # Устанавливаем заголовок экземпляра tkinter (*.title)
    root.geometry("765x450")                        # Устанавливаем размер экземпляра tkinter(*.geometry)
    root.resizable(False, False)                    # Устанавливаем ограничения изменеия размеров окна(*.resizable)
    root.mainloop()                                 # Запускаем основной цикл обработки событий(*.mainloop)
