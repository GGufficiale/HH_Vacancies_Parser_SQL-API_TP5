from src.cls_db_manager import DBManager
from utils.utils import create_tables, create_database, insert_data_in_tables

db_name = "termpaper"
create_database(db_name)
create_tables(db_name)
insert_data_in_tables(db_name)

db = DBManager("termpaper")
print("Привет, юзер! Раз ты здесь, то ты точно найдешь работу мечты :) "
      "Смотри, какие компании есть в нашей базе данных:")
print(db.get_companies_and_vacancies_count())

print(input("А так ты сможешь посмотреть на вакансии с зарплатой и ссылками на них. Нажми Enter"))
print(db.get_all_vacancies())

print(input("А так - узнать среднюю зарплату по всем вакансиям. Нажми Enter"))
print(db.get_avg_salary())

print(input("А тут - узнать, у каких вакансий зарплата выше средней. Нажми Enter"))
print(db.get_vacancies_with_higher_salary())

print("А здесь - найти работу мечты по ключевому слову. Вбей, что тебе нравится :)")
keyword = input()
print(db.get_vacancies_with_keyword(keyword))
