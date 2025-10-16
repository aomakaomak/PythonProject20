from psycopg2.extensions import connection, cursor


class DBManager:
    """Класс для работы с базой данных"""

    def __init__(self, cur: cursor, conn: connection):

        self.conn = conn
        self.cur = cur

    def get_companies_and_vacancies_count(self):
        """Выводим список компаний с количеством вакансий"""
        self.cur.execute(
            """SELECT DISTINCT employer_name, COUNT (*)
                            FROM employers
                            INNER JOIN vacancies USING (employer_id)
                            GROUP BY employer_name;"""
        )
        rows = self.cur.fetchall()
        for row in rows:
            print(f"В компании {row[0]} открыто {row[1]} вак.")

    def get_all_vacancies(self):
        """Выводим список всех вакансий"""
        self.cur.execute(
            """SELECT vacancy_id, vacancy_name, employer_name, salary, vacancy_link
                            FROM vacancies
                            INNER JOIN employers USING (employer_id);"""
        )
        rows = self.cur.fetchall()
        for row in rows:
            print(*row)

    def get_avg_salary(self):
        """Выводим среднюю зарплату"""
        self.cur.execute("""SELECT AVG(salary) FROM vacancies;""")
        rows = self.cur.fetchall()
        for row in rows:
            print("Средняя зарплата равна ")
            print(*row)

    def get_vacancies_with_higher_salary(self):
        """Выводим вакансии с зарплатой выше средней"""
        self.cur.execute(
            """SELECT * 
                            FROM vacancies
                            WHERE salary > (SELECT AVG(salary) FROM vacancies)
                            ORDER BY salary DESC
                            ;"""
        )
        rows = self.cur.fetchall()
        for row in rows:
            print(*row)

    def get_vacancies_with_keyword(self, keyword):
        """Выводим вакансии с ключевым словом в названии"""
        self.cur.execute(
            f"""SELECT * FROM vacancies
                            WHERE vacancy_name LIKE '%{keyword}%';"""
        )
        rows = self.cur.fetchall()
        for row in rows:
            print(*row)


# if __name__ == "__main__":
#
#     conn = psycopg2.connect(
#         host="localhost",
#         database="pythontask",
#         user="postgres",
#         password="yompks83new"
#     )
#     cur = conn.cursor()
#
#     test1 = DBManager(cur, conn)
#     test1.get_companies_and_vacancies_count()
#     test1.get_all_vacancies()
#     test1.get_avg_salary()
#     test1.get_vacancies_with_higher_salary()
#     test1.get_vacancies_with_keyword("курьер")
