import psycopg2
from utils.config import config
from src.cls_HHParser import HeadHunterParser


def create_database(db_name):
    """Метод для создания таблицы"""
    con = psycopg2.connect(dbname="postgres", **config())
    con.autocommit = True
    cur = con.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")
    cur.close()
    con.close()


def create_tables(db_name):
    """Метод для создания столбцов таблицы"""
    con = psycopg2.connect(dbname=db_name, **config())
    with con:
        with con.cursor() as cur:
            cur.execute("CREATE TABLE employers (id INTEGER PRIMARY KEY, name VARCHAR(150))")
            cur.execute("CREATE TABLE vacancies (id INTEGER PRIMARY KEY, name VARCHAR(150),"
                        "link VARCHAR(150), salary_from INTEGER, salary_to INTEGER,"
                        "employer INTEGER REFERENCES employers(id))")
    con.close()


def insert_data_in_tables(db_name):
    """Метод для заполнения таблицы базы данных"""
    hh = HeadHunterParser()
    employers = hh.get_employers()
    vacancies = hh.get_vacancies()
    con = psycopg2.connect(dbname=db_name, **config())
    with con:
        with con.cursor() as cur:
            for employer in employers:
                cur.execute("INSERT INTO employers VALUES (%s, %s)", (employer["id"], employer["name"]))
            for vacancy in vacancies:
                cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s)",
                            (vacancy["id"], vacancy["name"], vacancy["link"], vacancy["salary_from"],
                             vacancy["salary_to"], vacancy["employer"]))
    con.close()


insert_data_in_tables("course_work")
