import psycopg2
from typing import List

def create_db_employers() -> None:
    """Функция для создания таблицы "Employers" """

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employers (
        employer_id int PRIMARY KEY, 
        employer_name varchar (300)
        );
    """)
    conn.commit()


def create_db_vacancies():
    cur.execute("""
       CREATE TABLE IF NOT EXISTS vacancies (
           vacancy_id serial PRIMARY KEY, 
           vacancy_name varchar (300),
           employer_id int REFERENCES employers (employer_id)
           );
       """)
    conn.commit()







if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="pythontask",
        user="postgres",
        password="yompks83new"
    )
    cur = conn.cursor()

    create_db_employers()
    create_db_vacancies()

    cur.close()
    conn.close()