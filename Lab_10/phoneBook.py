import psycopg2, csv

# Параметры подключения
conn = psycopg2.connect(
    host = "localhost",
    port = 5432,            #Стандартный порт PostgreSQL
    database = "phoneBook", #Имя базы данных
    user = "postgres",      #Имя пользователя
    password = "yourPassword"           #Пароль
)

#Создаем курсор
cursor = conn.cursor()

#Переменные
id = 1
name = ""
file = ""
phone = ""
choice = 0
done = False

#Создаем цикл
while not done:
    print("""
Press 1 to insert data into phonebook
Press 2 to update data from phonebook
Press 3 to filter and view table data
Press 4 to delete data from phonebook
Press 0 to quit
""")
    choice = int(input())

    if choice == 1: #Чтобы добавить запись
        print("""
Press 1 to insert data through console
Press 2 to insert data through csv file
Press 0 to quit
""")
        choice = int(input())

        if choice == 1: #Добавляем через консоль
            print("Name: ")
            name = input()

            print("Phone number: ")
            phone = input()

            #Добавляем запись
            cursor.execute("""
                INSERT INTO phoneBook (name, phone)
                VALUES (%s, %s);
            """, (name, phone))
            conn.commit() #Коммитим

            print("Done!")
        elif choice == 2: #Добавляем через файл
            print("Write your csv file's name: ")
            file = input()

            #Открываем файл
            try:
                with open(f"phoneBook/{file}.csv", newline = '') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter = ';') #Читает файл как словарь
                    for row in reader:
                        name = row['name']
                        phone = row['phone']

                        #Добавляем запись
                        cursor.execute("""
                            INSERT INTO phoneBook (name, phone)
                            VALUES (%s, %s);
                        """, (name, phone))
                        conn.commit() #Коммитим
                
                print("Done")
            except:
                print("Can not find csv file")
        else: #
            done = True
                    
    elif choice == 2: #Чтобы обновить инфу
        cursor.execute("""
            SELECT * FROM phoneBook;
        """)
        info = cursor.fetchall()

        if info:
            #Выводим инфу
            for data in info:
                print("ID: " + str(data[0]) + "; Name: " + str(data[1]) + "; Phone number: " + str(data[2]))

            print("Your ID: ")
            id = int(input())

            #Выбираем все в нашей таблице
            cursor.execute("""
                SELECT * FROM phoneBook
                WHERE id = %s;
            """, (id,))
            info = cursor.fetchone() #Получаем одну запись

            if info:
                print("ID: " + str(info[0]) + "; Name: " + str(info[1]) + "; Phone number: " + str(info[2]))
                print("""Press 1 to change name
Press 2 to change phone number
Press 3 to change both of them
Press 0 to quit
""")
                choice = int(input())

                if choice == 1: #Обновляем имя
                    print("Name: ")
                    name = input()

                    #Обновляем запись
                    cursor.execute("""
                        UPDATE phoneBook
                        SET name = %s
                        WHERE id = %s;
                    """, (name, id))
                    conn.commit() #

                    print("Done")
                elif choice == 2: #Обновляем номер
                    print("Phone number: ")
                    phone = input()

                    cursor.execute("""
                        UPDATE phoneBook
                        SET phone = %s
                        WHERE id = %s;
                    """, (phone, id))
                    conn.commit()

                    print("Done")
                elif choice == 3: #Обновляем по имени и по номеру
                    print("Name: ")
                    name = input()

                    print("Phone number: ")
                    phone = input()

                    cursor.execute("""
                        UPDATE phoneBook
                        SET name = %s, phone = %s
                        WHERE id = %s;
                    """, (name, phone, id))
                    conn.commit()

                    print("Done")
                else:
                    done = True
            else: #Не нашли запись
                print("The entry does not exist")
        else: #Если таблица пуста
            print("Nothing to update")
    elif choice == 3: #Чтобы вывести отфильтрованную инфу
        cursor.execute("""
            SELECT * FROM phoneBook;
        """)
        info = cursor.fetchall()

        if info:
            for data in info:
                print("ID: " + str(data[0]) + "; Name: " + str(data[1]) + "; Phone number: " + str(data[2]))

            print("""
    Press 1 to filter by name
    Press 2 to filter by phone
    Press 3 to filter by both of them
    Press 0 to quit
    """)
            choice = int(input())

            if choice == 1: #Чтобы филтровать по имени
                print("Name: ")
                name = f"%{input()}%" #Паттерн

                cursor.execute("""
                    SELECT * FROM phoneBook
                    WHERE name ILIKE %s;
                """, (name,))
                info = cursor.fetchall()

                if info:
                    #Выводим инфу
                    for data in info:
                        print("ID: " + str(data[0]) + "; Name: " + str(data[1]) + "; Phone number: " + str(data[2]))
                else: #
                    print("Nothing found")
            elif choice == 2: #Чтобы филтровать по номеру
                print("Phone number: ")
                phone = f"%{input()}%" #Паттерн

                cursor.execute("""
                    SELECT * FROM phoneBook
                    WHERE phone LIKE %s;
                """, (phone,))
                info = cursor.fetchall()

                if info:
                    #Выводим инфу
                    for data in info:
                        print("ID: " + str(data[0]) + "; Name: " + str(data[1]) + "; Phone number: " + str(data[2]))
                else:
                    print("Not found") #Не нашли запись
            elif choice == 3: #Чтобы филтровать по имени и по номеру
                print("Name: ")
                name = f"%{input()}%"

                print("Phone number: ")
                phone = f"%{input()}%"

                cursor.execute("""
                    SELECT * FROM phoneBook
                    WHERE name ILIKE %s
                    AND phone LIKE %s;
                """, (name, phone))
                info = cursor.fetchall()

                if info:
                    for data in info:
                        print("ID: " + str(data[0]) + "; Name: " + str(data[1]) + "; Phone number: " + str(data[2]))
                else:
                    print("Nothing found")
            else:
                done = True
        else: #Если таблица пуста
            print("Nothing to filter")
    elif choice == 4: #Чтобы удалить инфу
        cursor.execute("""
            SELECT * FROM phoneBook;
        """)
        info = cursor.fetchall()

        if info:
            #Выводим инфу
            for data in info:
                print("ID: " + str(data[0]) + "; Name: " + str(data[1]) + "; Phone number: " + str(data[2]))
            
            print("""
Press 1 to delete by ID
Press 2 to delete by name
Press 3 to delete by phone number
Press 0 to quit
""")
            choice = int(input())

            if choice == 1: #Чтобы удалить по ID
                print("Enter your ID: ")
                id = int(input())

                cursor.execute("""
                    SELECT * FROM phoneBook
                    WHERE id = %s;
                """, (id,))
                info = cursor.fetchone()

                if info:
                    #Удаляем запись
                    cursor.execute("""
                        DELETE FROM phoneBook
                        WHERE id = %s;
                    """, (id,))
                    conn.commit()

                    print("Done")
                else: #Если ничего не было найдено
                    print("Not found")
            elif choice == 2: #Чтобы удалить по имени
                print("Name: ")
                name = input()

                cursor.execute("""
                    SELECT * FROM phoneBook
                    WHERE name = %s;
                """, (name,))
                info = cursor.fetchall()

                if len(info) > 1: #Если в таблице несколько похожих имен
                    for data in info:
                        print("ID: " + str(data[0]) + "; Name: " + str(data[1]) + "; Phone number: " + str(data[2]))

                    print("""
Press 1 to delete by ID
Press 2 to delete by phone number
Press 0 to quit
""")
                    choice = int(input())

                    if choice == 1: #Чтобы удалить по номеру
                        print("Enter your ID: ")
                        id = int(input())

                        cursor.execute("""
                            DELETE FROM phoneBook
                            WHERE id = %s;
                        """, (id,))
                        conn.commit()

                        print("Done")
                    if choice == 2: #Чтобы удалить по номеру
                        print("Phone number: ")
                        phone = input()

                        cursor.execute("""
                            SELECT * FROM phoneBook
                            WHERE name = %s AND phone = %s;
                        """, (name, phone))
                        info = cursor.fetchone()

                        if info:
                            cursor.execute("""
                                DELETE FROM phoneBook
                                WHERE name = %s AND phone = %s;
                            """, (name, phone))
                            conn.commit()

                            print("Done")
                        else:
                            print("The entry not found")
            elif choice == 3: #Чтобы удалить по номеру
                print("Phone number: ")
                phone = input()

                cursor.execute("""
                    SELECT * FROM phoneBook
                    WHERE phone = %s;
                """, (phone,))
                info = cursor.fetchone()

                if info:
                    cursor.execute("""
                        DELETE FROM phoneBook
                        WHERE phone = %s;
                    """, (phone,))
                    conn.commit()

                    print("Done")
                else:
                    print("Not found")
            else:
                done = True
        else: #Если в таблице ничего нет
            print("Nothing to delete")
    else: #Если нажали 0
        done = True

# Закрываем соединение
cursor.close()
conn.close()