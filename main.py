from classes import HeadHunterAPI, JSONSaver
from utils import sort_by_salary_min, sort_by_salary_max


def main():
    # keyword = input('Введите слово для поиска: ')
    keyword = "python"
    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies(keyword)

    json_saver = JSONSaver(keyword)
    json_saver.add_vacancies(hh_vacancies)
    data = json_saver.select()
    data = sort_by_salary_min(data)
    data = sort_by_salary_max(data)

    for row in data:
        print(row, end=f"\n\n{'='*200}\n\n")


if __name__ == "__main__":
    main()
