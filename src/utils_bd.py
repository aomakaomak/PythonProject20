import psycopg2
from typing import List
from src.utils_api import get_vacancies_per_id, get_id

def create_db_employers(cur, conn) -> None:
    """Функция для создания таблицы "Employers" """

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employers (
        employer_id int PRIMARY KEY, 
        employer_name varchar (300)
        );
    """)
    conn.commit()


def create_db_vacancies(cur, conn):
    cur.execute("""
       CREATE TABLE IF NOT EXISTS vacancies (
           vacancy_id serial PRIMARY KEY, 
           vacancy_name varchar (300),
           employer_id int REFERENCES employers (employer_id),
           city varchar(100),
           salary varchar(100),
           link varchar(300)
           );
       """)
    conn.commit()


def insert_db_employers(employers_list: List, cur, conn):
    for employer in employers_list:
        cur.execute("INSERT INTO employers (employer_id, employer_name) VALUES (%s, %s) ON CONFLICT (employer_id) DO UPDATE SET employer_name = EXCLUDED.employer_name;", (employer.get("employer_id"), employer.get("employer_name")))
        conn.commit()


def insert_db_vacancies(vacancy_list: List, cur, conn):
    for vacancy in vacancy_list:
        cur.execute("""INSERT INTO vacancies (vacancy_id, vacancy_name, employer_id, city, salary, link) 
                       VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (vacancy_id) DO UPDATE SET vacancy_name = EXCLUDED.vacancy_name;""",
                    (vacancy.get("vacancy_id"), vacancy.get("vacancy_name"), vacancy.get("employer_id"), vacancy.get("city"), vacancy.get("salary"), vacancy.get("link")))
        conn.commit()






if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="pythontask",
        user="postgres",
        password="yompks83new"
    )
    cur = conn.cursor()

    # create_db_employers()
    # create_db_vacancies()

    # employers_list = ["МТС", "Яндекс", "Сбербанк"]
    # insert_db_employers(employers_list)



    cur.close()
    conn.close()