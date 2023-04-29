from classes import HeadHunterAPI, JSONSaver


def main():
    # keyword = input('Введите слово для поиска: ')
    keyword = "python"
    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies(keyword)

    json_saver = JSONSaver(keyword)
    json_saver.add_vacancies(hh_vacancies)


if __name__ == "__main__":
    main()
