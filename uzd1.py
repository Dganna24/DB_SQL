import csv
import sqlite3  # Замените на соответствующий драйвер для вашей БД

import cursor

from main import select_command
print('1\n')
select_command("""SELECT ASMENSKODAS, VARDAS, PAVARDE FROM DARBUOTOJAS
WHERE GIMIMOMETAI = '1988-07-20';""")

print('2\n')
select_command("""SELECT * FROM DARBUOTOJAS
WHERE GIMIMOMETAI < '1988-07-29';""")

print('3\n')
select_command("""SELECT VARDAS, PAVARDE, DIRBANUO, GIMIMOMETAI FROM DARBUOTOJAS
WHERE DIRBANUO BETWEEN '2009-10-30' AND '2012-11-11';""")

print('4\n')
select_command("""SELECT VARDAS, PAVARDE, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID FROM DARBUOTOJAS
WHERE PROJEKTAS_ID IN (2, 3);""")

print('5\n')
select_command("""SELECT VARDAS, PAVARDE, ASMENSKODAS FROM DARBUOTOJAS
WHERE ASMENSKODAS LIKE '4%';""")

print('6\n')
select_command("""SELECT vardas, strftime('%Y', GIMIMOMETAI) AS GIMIMOMETAI FROM DARBUOTOJAS WHERE GIMIMOMETAI LIKE '%-12';""")


print('7\n')
select_command("""SELECT * FROM PROJEKTAS WHERE PAVADINIMAS LIKE '__u%';""")


# Подключение к базе данных
connection = sqlite3.connect('Pavyzdine.db')
cursor = connection.cursor()

# Получение данных из таблицы (замените 'ваша_таблица' на фактическое имя таблицы)
cursor.execute("SELECT * FROM DARBUOTOJAS")
data = cursor.fetchall()

# Создание CSV файла
with open('select.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Запись заголовков (проверьте, чтобы названия соответствовали колонкам в таблице)
    writer.writerow(['ASMENSKODAS', 'VARDAS', 'PAVARDE', 'DIRBANUO', 'GIMIMOMETAI', 'PAREJGOS', 'SKYRIUS_PAVADINIMAS', 'PROJEKTAS_ID', 'DEPARTAMENTAS_ID', 'ATLYGINIMAS'])

    # Запись данных
    writer.writerows(data)

# Закрытие соединения
connection.close()