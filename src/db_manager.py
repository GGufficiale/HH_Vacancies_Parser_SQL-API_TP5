import psycopg2
from utils.config import config


class DBManager:
    def __init__(self, db_name):
        self.__db_name = db_name

    def execute_query(self, query):
        con = psycopg2.connect(dbname=self.__db_name, **config())
        with con:
            with con.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()

            con.close()
            return result

    def get_all_vacancies(self):
        query = "SELECT * FROM vacancies " \
                "JOIN employers ON vacancies.employer = employers.id"
        return self.execute_query(query)

