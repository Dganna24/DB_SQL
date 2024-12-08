from main import select_command

print('8\n')
# Isrinkite visus darbuotojus is lentelés DARBUOTOJAS, kuriems nepaskirtos jokios pareigos.
select_command("""SELECT * FROM DARBUOTOJAS WHERE pareigos IS NULL;""")

print('9\n')
#Isrinkite duomenis apie darbuotoja (varda, pavarde, nuo kada dirba ir pareigas) kad tenkintu salygas:
# (dirba nuo 2011-02-12 ir ju pareigos yra Programuotojai).
select_command("""SELECT VARDAS, PAVARDE, DIRBANUO, PAREIGOS 
                FROM DARBUOTOJAS WHERE DIRBANUO = '2011-02-12' 
                AND PAREIGOS LIKE 'Programuotoj%';""")

print('10\n')
#Isrinkite duomenis apie darbuotojus (varda, pavarde, skyriaus pavadinima ir projekto ID) is
# lentelés DARBUOTOJAS su salyga, kad jie butu is Java skyriaus arba 1 projekto.

select_command("""SELECT VARDAS, PAVARDE, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID FROM DARBUOTOJAS 
                WHERE SKYRIUS_PAVADINIMAS = 'Java' OR PROJEKTAS_ID = 1;""")

print('11\n')
#Isrinkite visus darbuotoju vardus isskyrus tuos, kuriu vardai prasideda raide 's'.
select_command("""SELECT VARDAS 
                FROM DARBUOTOJAS 
                WHERE VARDAS NOT LIKE 's%';""")

print('12\n')
#Isrinkite duomenis ( varda, dirba nuo kada ir gimimo metus) is lentelès "DARBUOTOJAS" ,
# apie visus darbuotojus tik ne tuos, kurie isidarbino nuo 2009m spalio 30d iki 2012m lapkricio 11d.
select_command("""SELECT VARDAS, DIRBANUO, GIMIMOMETAI 
                FROM DARBUOTOJAS 
                WHERE DIRBANUO NOT BETWEEN '2009-10-30' AND '2012-11-11';""")

print('13\n')
#Išrinkite duomenis apie darbuotojus (varda, pavarde ir gimimo metus) is
# lentelés DARBUOTOJAS ir isrikiuokite visus duomenis nuo seniausio mogaus iki jauniausio.
select_command("""SELECT VARDAS, PAVARDE, GIMIMOMETAI 
                FROM DARBUOTOJAS 
                ORDER BY GIMIMOMETAI ASC;""")

print('14\n')
# Isrinkite duomenis apie darbuotojus (varda, pavardeir gimimo metus) is
# lenteles DARBUOTOJAS ir isrikiuokite visus duomenis nuo jauniausio mogaus iki seniausio.
select_command("""SELECT VARDAS, PAVARDE, GIMIMOMETAI 
                FROM DARBUOTOJAS 
                ORDER BY GIMIMOMETAI DESC;""")
import sqlite3
import pandas as pd

# Подключение к базе данных
connection = sqlite3.connect('Pavyzdine.db')

# Создание пустого списка для хранения DataFrame
all_data = []

# 8. Isrinkite visus darbuotojus is lentelės DARBUOTOJAS, kuriems nepaskirtos jokios pareigos.
query8 = "SELECT * FROM DARBUOTOJAS WHERE PAREIGOS IS NULL;"
data8 = pd.read_sql_query(query8, connection)
data8.insert(0, 'Заголовок', 'Nadleisto darbuotojai')
all_data.append(data8)

# 9. Duomenis apie darbuotoja (varda, pavarde, nuo kada dirba ir pareigas)
query9 = "SELECT VARDAS, PAVARDE, DIRBANUO, PAREIGOS FROM DARBUOTOJAS WHERE DIRBANUO >= '2011-02-12' AND PAREIGOS LIKE 'Programuotojai%';"
data9 = pd.read_sql_query(query9, connection)
data9.insert(0, 'Заголовок', 'Programuotojai')
all_data.append(data9)

# 10. Duomenis apie darbuotojus (varda, pavarde, skyriaus pavadinima ir projekto ID)
query10 = "SELECT VARDAS, PAVARDE, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID FROM DARBUOTOJAS WHERE SKYRIUS_PAVADINIMAS = 'Java' OR PROJEKTAS_ID = 1;"
data10 = pd.read_sql_query(query10, connection)
data10.insert(0, 'Заголовок', 'Java skyrius arba Projektas 1')
all_data.append(data10)

# 11. Visus darbuotojų vardus, išskyrus tuos, kurių vardai prasideda raide 's'.
query11 = "SELECT VARDAS FROM DARBUOTOJAS WHERE VARDAS NOT LIKE 's%';"
data11 = pd.read_sql_query(query11, connection)
data11.insert(0, 'Заголовок', 'Vardai be s')
all_data.append(data11)

# 12. Duomenis apie visus darbuotojus, tik ne tuos, kurie įsidarbino nuo 2009m. spalio 30d. iki 2012m. lapkričio 11d.
query12 = "SELECT VARDAS, DIRBANUO, GIMIMOMETAI FROM DARBUOTOJAS WHERE DIRBANUO NOT BETWEEN '2009-10-30' AND '2012-11-11';"
data12 = pd.read_sql_query(query12, connection)
data12.insert(0, 'Заголовок', 'Darbuotojai ne laikotarpis')
all_data.append(data12)

# 13. Visus duomenis nuo seniausio žmogaus iki jauniausio.
query13 = "SELECT VARDAS, PAVARDE, GIMIMOMETAI FROM DARBUOTOJAS ORDER BY GIMIMOMETAI ASC;"
data13 = pd.read_sql_query(query13, connection)
data13.insert(0, 'Заголовок', 'Seniausias iki jauniausio')
all_data.append(data13)

# 14. Duomenis apie darbuotojus (varda, pavarde ir gimimo metus)
query14 = "SELECT VARDAS, PAVARDE, GIMIMOMETAI FROM DARBUOTOJAS ORDER BY GIMIMOMETAI DESC;"
data14 = pd.read_sql_query(query14, connection)
data14.insert(0, 'Заголовок', 'Jauniausias iki seniausio')
all_data.append(data14)

# Закрытие соединения
connection.close()

# Объединение всех DataFrame в один
final_data = pd.concat(all_data, ignore_index=True)

# Сохранение в один CSV файл
final_data.to_csv('darbuotojai_su_zagovlovi.csv', index=False)

print("Все данные сохранены в один CSV файл 'darbuotojai.csv'.")