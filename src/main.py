import psycopg2
from src.utils_api import get_vacancies_per_id, get_id
from src.utils_bd import create_db_employers, create_db_vacancies, insert_db_employers, insert_db_vacancies

conn = psycopg2.connect(
    host="localhost",
    database="pythontask",
    user="postgres",
    password="yompks83new"
)
cur = conn.cursor()

employers_list = ["МТС", "Яндекс", "Сбербанк"]

employers_id = []
for employer in employers_list:
    employers_id.append(get_id(employer))
print(employers_id)


vacancy_list = []
for id in employers_id:
    vacancy_list.extend(get_vacancies_per_id(id))
print(vacancy_list)

create_db_employers(cur, conn)
create_db_vacancies(cur, conn)

insert_db_employers(vacancy_list, cur, conn)
insert_db_vacancies(vacancy_list, cur, conn)


cur.close()
conn.close()

