from classes import HeadHunterAPI


def main():
    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies("Python")


if __name__ == "__main__":
    main()
