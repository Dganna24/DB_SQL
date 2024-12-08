import sqlite3
import pandas as pd

# Подключение к базе данных
connection = sqlite3.connect('Pavyzdine.db')

# 8. Isrinkite visus darbuotojus is lentelės DARBUOTOJAS, kuriems nepaskirtos jokios pareigos.
query8 = "SELECT * FROM DARBUOTOJAS WHERE PAREIGOS IS NULL;"
data8 = pd.read_sql_query(query8, connection)

# 9. Duomenis apie darbuotoja (varda, pavarde, nuo kada dirba ir pareigas) kad tenkintu salygas: (dirba nuo 2011-02-12 ir ju pareigos yra Programuotojai).
query9 = "SELECT VARDAS, PAVARDE, DIRBANUO, PAREIGOS FROM DARBUOTOJAS WHERE DIRBANUO = '2011-02-12' AND PAREIGOS LIKE 'Programuotoj%';"
data9 = pd.read_sql_query(query9, connection)

# 10. Duomenis apie darbuotojus (varda, pavarde, skyriaus pavadinima ir projekto ID)
query10 = "SELECT VARDAS, PAVARDE, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID FROM DARBUOTOJAS WHERE SKYRIUS_PAVADINIMAS = 'Java' OR PROJEKTAS_ID = 1;"
data10 = pd.read_sql_query(query10, connection)

# 11. Visus darbuotojų vardus, išskyrus tuos, kurių vardai prasideda raide 's'.
query11 = "SELECT VARDAS FROM DARBUOTOJAS WHERE VARDAS NOT LIKE 's%';"
data11 = pd.read_sql_query(query11, connection)

# 12. Duomenis apie visus darbuotojus, tik ne tuos, kurie įsidarbino nuo 2009m. spalio 30d. iki 2012m. lapkričio 11d.
query12 = "SELECT VARDAS, DIRBANUO, GIMIMOMETAI FROM DARBUOTOJAS WHERE DIRBANUO NOT BETWEEN '2009-10-30' AND '2012-11-11';"
data12 = pd.read_sql_query(query12, connection)

# 13. Visus duomenis nuo seniausio žmogaus iki jauniausio.
query13 = "SELECT VARDAS, PAVARDE, GIMIMOMETAI FROM DARBUOTOJAS ORDER BY GIMIMOMETAI ASC;"
data13 = pd.read_sql_query(query13, connection)

# 14. Duomenis apie darbuotojus (varda, pavarde ir gimimo metus)
query14 = "SELECT VARDAS, PAVARDE, GIMIMOMETAI FROM DARBUOTOJAS ORDER BY GIMIMOMETAI DESC;"
data14 = pd.read_sql_query(query14, connection)

# Закрытие соединения
connection.close()

# Создание Excel файла с листами для каждого запроса

# Создание Excel файла с листами для каждого запроса
with pd.ExcelWriter('darbuotojai.xlsx') as writer:
    data8.to_excel(writer, sheet_name='Nepaskirtos pareigos', index=False)
    data9.to_excel(writer, sheet_name='Programuotojai', index=False)
    data10.to_excel(writer, sheet_name='Java skyrius arba Projektas 1', index=False)
    data11.to_excel(writer, sheet_name='Vardai be s', index=False)
    data12.to_excel(writer, sheet_name='Darbuotojai-laikotarpis', index=False)
    data13.to_excel(writer, sheet_name='Seniausias iki jauniausio', index=False)
    data14.to_excel(writer, sheet_name='Jauniausias iki seniausio', index=False)

print("Данные сохранены в 'darbuotojai.xlsx'")