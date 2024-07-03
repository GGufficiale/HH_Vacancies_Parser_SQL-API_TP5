import psycopg2
from utils.config import config


class DBManager:
    def __init__(self, db_name):
        self.__db_name = db_name

    def execute_query(self, query):
        """Метод для подсоединения к БД"""
        con = psycopg2.connect(dbname=self.__db_name, **config())
        with con:
            with con.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()

        con.close()
        return result

    def get_companies_and_vacancies_count(self):
        """Метод получает список всех компаний и количество вакансий у каждой компании"""
        query = ("SELECT employers.name, COUNT(employers.name) FROM vacancies "
                 "JOIN employers ON vacancies.employer = employers.id "
                 "GROUP BY employers.name")
        return self.execute_query(query)

    def get_all_vacancies(self):
        """Метод получает список всех вакансий с указанием названия компании, вакансии и зп и ссылки на вакансию"""
        query = "SELECT * FROM vacancies " \
                "JOIN employers ON vacancies.employer = employers.id"
        return self.execute_query(query)

    def get_avg_salary(self):
        """Метод получает среднюю зарплату по вакансиям"""
        query = "SELECT AVG(salary_from) FROM vacancies"
        return int(self.execute_query(query)[0][0])

    def get_vacancies_with_higher_salary(self):
        """Метод получает список всех вакансий, у которых зп выше средней по всем вакансиям"""
        avg_salary = str(self.get_avg_salary())
        query = f"SELECT * FROM vacancies WHERE salary_from > {avg_salary}"
        return self.execute_query(query)

    def get_vacancies_with_keyword(self, keyword):
        """Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова (e.g. python)"""
        query = f"SELECT * FROM vacancies WHERE name LIKE '%{keyword}%'"
        return self.execute_query(query)
