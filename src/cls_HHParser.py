import requests


class HeadHunterParser:
    """Класс для работы с НН API"""

    @staticmethod
    def get_response():
        """Запрос на НН API и возврат списка работодателей"""
        params = {"sort_by": "by_vacancies_open", "per_page": 10}
        response = requests.get("https://api.hh.ru/employers", params=params)
        if response.status_code == 200:
            # Если статус-код - 200, то всё ок, запрос проходит
            return response.json()["items"]

    def get_employers(self) -> list:
        """Выбор 10 интересующих компаний"""
        data = self.get_response()
        # loved_employers = ['Пятёрочка', 'Магнит']
        employers = []
        for employer in data:
            # if employer["name"] in loved_employers:
            #     loved_employers.append({"id": employer["id"], "name": employer["name"]})
            employers.append({"id": employer["id"], "name": employer["name"]})
        return employers #loved_employers[2:]

    def get_vacancies(self) -> list:
        """Получение вакансий в формате json"""
        employers = self.get_employers()
        vacancies = []
        for employer in employers:
            params = {"employer_id": employer["id"]}
            response = requests.get("https://api.hh.ru/vacancies", params=params)
            if response.status_code == 200:
                filtered_vacancies = self.filter_vacancies(response.json()["items"])
                vacancies.extend(filtered_vacancies)
        return vacancies

    @staticmethod
    def filter_vacancies(vacancies) -> list:
        """Метод фильтрации значений (вакансий) из массы с НН по выбранным нами параметрам"""
        filtered_vacancies = []
        for vacancy in vacancies:
            if vacancy["salary"] is None:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            filtered_vacancies.append({
                "id": vacancy["id"],
                "name": vacancy["name"],
                "link": vacancy["alternate_url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "employer": vacancy["employer"]["id"]
            })
        return filtered_vacancies


hh = HeadHunterParser()
# """Проверка вывода отфильтрованных работодателей по id"""
# print(hh.get_response())

"""Проверка вывода инфо о работодателе в формате id + name"""
print(hh.get_employers())

# """Проверка вывода инфо о вакансиях в выбранном нами формате"""
# print(hh.get_vacancies())
