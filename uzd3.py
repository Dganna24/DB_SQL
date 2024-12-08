from main import select_command

#15. Isrinkite is lentelés DARBUOTOJAS projekto id kuris butu minimalus skaiius ir maksimalus skaicius.
print('15\n')
select_command("""SELECT MIN(projektas_id) AS minimalus_id, 
    MAX(projektas_id) AS maksimalus_id FROM DARBUOTOJAS;""")

#16. Isrinkite duomenis apie projekta ir kiek tame projekte yra priskirta moniu is
# lentelés DARBUOTOJAS (projekto numeris ir skaitius kiek dalyvauja moniu).
print('16\n')
select_command("""SELECT projektas_id, COUNT(*) AS dalyviu_skaicius 
FROM DARBUOTOJAS GROUP BY projektas_id;""")

#17. Isrinkite duomenis (projekto numeris, pareigos, skaicius) is lentelés
# DARBUOTOJAS kiek dirba programuotoju kiekvienam projekte.
print('17\n')
select_command("""SELECT PROJEKTAS_ID, PAREIGOS, COUNT(*) AS skaicius 
FROM DARBUOTOJAS WHERE PAREIGOS LIKE 'Programuotoj%' GROUP BY PROJEKTAS_ID, PAREIGOS;""")

#18. #17 punkto uklausa pataisykite taip, kad rodytu tik tuos projektus, kur dirba bent 2 darbuotojai.
print('18\n')
select_command("""SELECT projektas_id, pareigos, COUNT(*) AS skaicius 
FROM DARBUOTOJAS WHERE pareigos = 'Programuotojas' 
GROUP BY projektas_id, pareigos HAVING COUNT(*) >= 2;""")

import pandas as pd
import sqlite3  # или другую библиотеку, если используете другую базу данных

# Подключение к базе данных
conn = sqlite3.connect('Pavyzdine.db')  # замените 'your_database.db' на ваш файл базы данных

# Выполнение SQL-запроса
query = """
SELECT PROJEKTAS_ID, PAREIGOS, COUNT(*) AS skaicius 
FROM DARBUOTOJAS 
WHERE PAREIGOS LIKE 'Programuotoj%' 
GROUP BY PROJEKTAS_ID, PAREIGOS;
"""

# Чтение данных в DataFrame
df = pd.read_sql_query(query, conn)

# Сохранение в CSV файл
df.to_csv('seleсt3.csv', index=False)

# Закрытие подключения
conn.close()