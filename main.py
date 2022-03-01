import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import time
import datetime

start_time = time.time()


def scrap_google():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }

    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    urls_valid_pages = []
    urls_invalid_pages = []
    search = []
    header = []

    need_year = input("Введите нужный год:")

    try:
        if need_year != "все":
            i = int(need_year) # в 2022 году пагинация отличается, стрелка находится на -2 месте
            count = 0
            url = f"https://www.hse.ru/edu/vkr/?faculty=120026365&year={i}"
            print(f"Данные за {i}")
            print("=" * 5)
            time.sleep(3)
            r = requests.get(url=url, headers=headers)

            with open(f"index_{i}.html", "w", encoding="utf-8") as file:
                file.write(r.text)

            with open(f"index_{i}.html", encoding="utf-8") as file:
                site = file.read()

            soup = BeautifulSoup(site, "lxml")
            if i != 2022:
                pages_count = int(soup.find("div", class_="letterlist").find_all("a")[-1].text.strip())
                print(f"Найдено страниц: {pages_count}")
                print("=" * 25)

                time.sleep(5)
                for page in range(1, pages_count + 1):
                    url = f"https://www.hse.ru/edu/vkr/?faculty=120026365&year={i}&page={page}"
                    r = requests.get(url=url, headers=headers)

                    count += 1

                    with open(f"index_{i}_{count}.html", "w", encoding="utf-8") as file:
                        file.write(r.text)

                    with open(f"index_{i}_{count}.html", encoding="utf-8") as file:
                        site = file.read()

                    soup = BeautifulSoup(site, "lxml")

                    names = soup.find_all("li", class_="vkr-list__item vkr-card")
                    for item in names:

                        year = item.find_all("span", class_="vkr-card__value")[-1].text.strip()
                        title = item.find("h3").find("a").text.strip()
                        search.append([title, year])

            else:

                pages_count = int(soup.find("div", class_="letterlist").find_all("a")[-2].text.strip())
                print(f"Найдено страниц: {pages_count}")
                print("=" * 25)
                time.sleep(5)
                for page in range(1, pages_count + 1):
                    url = f"https://www.hse.ru/edu/vkr/?faculty=120026365&year={i}&page={page}"

                    count += 1

                    with open(f"index_{i}_{count}.html", "w", encoding="utf-8") as file:
                        file.write(r.text)

                    with open(f"index_{i}_{count}.html", encoding="utf-8") as file:
                        site = file.read()

                    soup = BeautifulSoup(site, "lxml")

                    names = soup.find_all("li", class_="vkr-list__item vkr-card")
                    for item in names:
                        year = item.find_all("span", class_="vkr-card__value")[-1].text.strip()
                        title = item.find("h3").find("a").text.strip()
                        search.append([title, year])
        else:
            for i in range(2015, 2023):
                count = 0
                url = f"https://www.hse.ru/edu/vkr/?faculty=120026365&year={i}"
                print(f"Данные за {i}")
                print("=" * 5)
                time.sleep(3)
                r = requests.get(url=url, headers=headers)

                with open(f"index_{i}.html", "w", encoding="utf-8") as file:
                    file.write(r.text)

                with open(f"index_{i}.html", encoding="utf-8") as file:
                    site = file.read()

                soup = BeautifulSoup(site, "lxml")
                if i != 2022:
                    pages_count = int(soup.find("div", class_="letterlist").find_all("a")[-1].text.strip())
                    print(f"Найдено страниц: {pages_count}")
                    print("=" * 25)

                    time.sleep(5)
                    for page in range(1, pages_count + 1):
                        url = f"https://www.hse.ru/edu/vkr/?faculty=120026365&year={i}&page={page}"
                        r = requests.get(url=url, headers=headers)

                        count += 1

                        with open(f"index_{i}_{count}.html", "w", encoding="utf-8") as file:
                            file.write(r.text)

                        with open(f"index_{i}_{count}.html", encoding="utf-8") as file:
                            site = file.read()

                        soup = BeautifulSoup(site, "lxml")

                        names = soup.find_all("li", class_="vkr-list__item vkr-card")
                        for item in names:
                            year = item.find_all("span", class_="vkr-card__value")[-1].text.strip()
                            title = item.find("h3").find("a").text.strip()
                            search.append([title, year])

                else:

                    pages_count = int(soup.find("div", class_="letterlist").find_all("a")[-2].text.strip())
                    print(f"Найдено страниц: {pages_count}")
                    print("=" * 25)
                    time.sleep(5)
                    for page in range(1, pages_count + 1):
                        url = f"https://www.hse.ru/edu/vkr/?faculty=120026365&year={i}&page={page}"

                        count += 1

                        with open(f"index_{i}_{count}.html", "w", encoding="utf-8") as file:
                            file.write(r.text)

                        with open(f"index_{i}_{count}.html", encoding="utf-8") as file:
                            site = file.read()

                        soup = BeautifulSoup(site, "lxml")

                        names = soup.find_all("li", class_="vkr-list__item vkr-card")
                        for item in names:
                            year = item.find_all("span", class_="vkr-card__value")[-1].text.strip()
                            title = item.find("h3").find("a").text.strip()
                            search.append([title, year])


        header = (['title', 'year'])

        df = pd.DataFrame(search, columns=header)
        df.to_csv("work_2.csv", sep=";", encoding="utf-8-sig")

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    scrap_google()
    finish_time = time.time() - start_time
    print(f"Затраченное на работу скрипта время: {finish_time}")