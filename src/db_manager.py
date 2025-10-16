import psycopg2


class DBManager:

    def __init__(self, cur, conn):

        self.conn = conn
        self.cur = cur

    def get_companies_and_vacancies_count(self):
        self.cur.execute ("""SELECT DISTINCT employer_name, COUNT (*)
                            FROM employers
                            INNER JOIN vacancies USING (employer_id)
                            GROUP BY employer_name""")
        rows = self.cur.fetchall()
        for row in rows:
            print(f"В компании {row[0]} открыто {row[1]} вак.")


    def get_all_vacancies(self):
        self.cur.execute("""SELECT vacancy_id, vacancy_name, employer_name, salary, vacancy_link
                            FROM vacancies
                            INNER JOIN employers USING (employer_id)""")
        rows = self.cur.fetchall()
        for row in rows:
            print(*row)





if __name__ == "__main__":

    conn = psycopg2.connect(
        host="localhost",
        database="pythontask",
        user="postgres",
        password="yompks83new"
    )
    cur = conn.cursor()

    test1 = DBManager(cur, conn)
    test1.get_companies_and_vacancies_count()
    test1.get_all_vacancies()