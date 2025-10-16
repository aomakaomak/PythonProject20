from src.final_func_for_main import create_db_for_our_companies
import psycopg2
from db_manager import DBManager


# Создаем наши базы данных
employers_list = ["МТС", "Яндекс", "Сбербанк", "Газпром", "Аэрофлот"]
create_db_for_our_companies(employers_list)


conn = psycopg2.connect(
        host="localhost",
        database="pythontask",
        user="postgres",
        password="yompks83new"
    )
cur = conn.cursor()

# Реализуем наши методы
test1 = DBManager(cur, conn)
test1.get_companies_and_vacancies_count()
test1.get_all_vacancies()
test1.get_avg_salary()
test1.get_vacancies_with_higher_salary()
test1.get_vacancies_with_keyword("курьер")





