import requests
from typing import List

def get_id(company_name: str) -> int:
    """Получаем ID компании. Так как их в выдаче много, то берем с максиммальным
    количеством вакансий"""
    headers = {"User-Agent": "demo-script/1.0"}
    resp = requests.get("https://api.hh.ru/employers",
                        params={"text": company_name, "only_with_vacancies": "true", "per_page": 50},
                        headers=headers)
    if resp.status_code != 200:
        raise Exception(f"GitHub API error: {resp.status_code}")
    data = resp.json()["items"]

    # Находим работодателя с наибольшим количеством вакансий
    best = max(data, key=lambda x: x["open_vacancies"])
    print("Основной работодатель:", best["name"])
    print("ID:", best["id"])
    print("Вакансий:", best["open_vacancies"])
    print("URL:", best["alternate_url"])
    print(best)
    return best["id"]

def get_vacancies_per_id(id: int) -> List:
    """Формируем список вакансий компании на основе ID"""
    headers = {"User-Agent": "demo-script/1.0"}
    url = f"https://api.hh.ru/vacancies?employer_id={id}"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f"GitHub API error: {resp.status_code}")
    data = resp.json()["items"]
    vacancy_list = []
    for vacancy in data:
        if not vacancy["salary"]:
            salary = 0
        else:
            salary = vacancy.get("salary").get("from")
        vacancy_dict = {
            "vacancy_id": vacancy.get("id"),
            "vacancy_name": vacancy.get("name"),
            "city": vacancy.get("area").get("name"),
            "salary": salary,
            "link": vacancy.get("alternate_url"),
            "employer_id": id,
            "employer_name": vacancy.get("employer").get("name")
        }
        vacancy_list.append(vacancy_dict)
    return vacancy_list



if __name__ == "__main__":
    print(get_id("МТС"))
    print(get_vacancies_per_id(2537115)[0])