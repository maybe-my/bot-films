# TODO: Получить сылку фильма.
# запрос https://rezka.ag/search/?do=search&subaction=search&q="название"
# "Фильм: {res['title']}. О фильме: {res['year']} . сылка {res['URL']} \n Фото: {res['img']}"
import requests
from bs4 import BeautifulSoup


def get_film(title):
    url_search = f"https://rezka.ag/search/?do=search&subaction=search&q={title}"
    page = 1
    max_page = 2
    while page < max_page:
        # url = 'https://toster.ru/questions/latest?page=' + str(page)
        source_code = requests.get(url_search)
        soup = BeautifulSoup(source_code.text, 'html.parser')
        items = soup.find_all('div', class_="b-content__inline_item")
        result = []
        for item in items:
            result.append({
                'title': item.find("a").text.strip(),
                'URL': item.find("a").get('href').strip(),
                'year': item.find('div').text.strip(),
                'img': item.find('img').get('src')
            })
            for res in result:
                print(f"Фильм: {res['title']}. О фильме: {res['year']} . Смотреть --> {res['URL']} \n Фото: {res['img']}")
            # print(title.text.strip(), title.get('href'))  # Первый элемент - название, второй - ссылка.
        page += 1


get_film("кто я")
