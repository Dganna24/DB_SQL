import sqlite3

'''def create_table(komanda):
    conn = sqlite3.connect('duomenu_baze.db')
    c = conn.cursor()
    c.execute(komanda)
    conn.commit()
    conn.close()

def instert_in_table(komanda, values):
    conn = sqlite3.connect('duomenu_baze.db')
    c = conn.cursor()
    c.execute(komanda, values)
    conn.commit()
    conn.close()'''
def select_command(komanda):
    conn = sqlite3.connect('Pavyzdine.db')
    c = conn.cursor()
    c.execute(komanda)
    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    conn.close()
def update_command(komanda):
    conn = sqlite3.connect('Pavyzdine.db')
    c = conn.cursor()
    c.execute(komanda)
    conn.commit()
    conn.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    select_command("""SELECT name FROM sqlite_master
                        WHERE type = 'table'
                        ORDER BY name;""")
    select_command("""PRAGMA table_info(DARBUOTOJAS)""")
    print("\n")
    select_command("""SELECT * FROM DARBUOTOJAS""")
    #select_command("""SELECT * FROM DARBUOTOJAS WHERE PROJEKTAS_ID = 2""")
    #select_command("""SELECT MAX(DIRBANUO), MIN(DIRBANUO) FROM DARBUOTOJAS""")

    update_command("ALTER TABLE DARBUOTOJAS ADD COLUMN ATLYGINIMAS REAL;")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 5000 WHERE PROJEKTAS_ID = 1 AND DEPARTAMENTAS_ID = 1;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 4000 WHERE PROJEKTAS_ID = 1 AND DEPARTAMENTAS_ID = 2;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 2000 WHERE PROJEKTAS_ID = 1 AND DEPARTAMENTAS_ID = 3;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 3500 WHERE PROJEKTAS_ID = 2 AND DEPARTAMENTAS_ID = 1;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 4500 WHERE PROJEKTAS_ID = 2 AND DEPARTAMENTAS_ID = 2;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 5500 WHERE PROJEKTAS_ID = 2 AND DEPARTAMENTAS_ID = 3;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 2500 WHERE PROJEKTAS_ID = 3 AND DEPARTAMENTAS_ID = 1;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 3300 WHERE PROJEKTAS_ID = 3 AND DEPARTAMENTAS_ID = 2;""")
    update_command("""UPDATE DARBUOTOJAS SET ATLYGINIMAS = 3200 WHERE PROJEKTAS_ID = 3 AND DEPARTAMENTAS_ID = 3;""")

    select_command("""SELECT * FROM DARBUOTOJAS""")
    print("\n")
    select_command("""SELECT PAREIGOS, VARDAS, SUM(ATLYGINIMAS) BendraSuma FROM DARBUOTOJAS
                        WHERE PAREIGOS NOT LIKE 'Projekt% vadov%'
                        GROUP BY PAREIGOS;""")
    print("\n")
    '''select_command("""SELECT PAREIGOS, VARDAS, SUM(ATLYGINIMAS) BendraSuma FROM DARBUOTOJAS
                            WHERE PAREIGOS NOT LIKE 'Programuotoj%'
                            GROUP BY PAREIGOS HAVING SUM(ATLYGINIMAS) > 5000 ORDER BY SUM(ATLYGINIMAS);""")

    select_command("""PRAGMA table_info(DEPARTAMENTAS)""")'''

    select_command("""SELECT * FROM DARBUOTOJAS, DEPARTAMENTAS WHERE ATLYGINIMAS > 3000""")
    select_command("""SELECT VARDAS, PAVARDE, ATLYGINIMAS, PAVADINIMAS FROM DARBUOTOJAS W LEFT JOIN DEPARTAMENTAS D
                           ON W.DEPARTAMENTAS_ID = D.ID WHERE ATLYGINIMAS > 3000""")

    '''create_table("""CREATE TABLE IF NOT EXISTS darbuotojai (
                    vardas TEXT,
                    pavarde TEXT,
                    alyginimas INTEGER)""")
    vardas = "Petras"
    instert_in_table("""INSERT INTO darbuotojai (vardas) VALUES (:vardas)""", {"vardas": vardas})'''