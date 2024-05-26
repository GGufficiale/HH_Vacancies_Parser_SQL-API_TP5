from src.db_manager import DBManager
from utils.utils import create_tables, create_database, insert_data_in_tables

db_name = "course_work"
create_database(db_name)
create_tables(db_name)
insert_data_in_tables(db_name)

db = DBManager("course_work")
print(db.get_all_vacancies())
