import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'works', 'интернет']


resp = requests.get('https://habr.com/ru/all/')
if resp.status_code != 200:
    raise Exception('bad response')
text = resp.text


def soup_scrapping():
    soup = BeautifulSoup(text, features='html.parser')
    previews = soup.find_all('article', class_='post post_preview')
    for preview in previews:
        prew = [x.text.strip().lower() for x in preview.find_all('p')]
        for p in prew:
            if any(kw in p for kw in KEYWORDS):
                date_el = preview.find('span', class_='post__time')
                date = date_el.text.strip()
                title_el = preview.find('a', class_='post__title_link')
                title = title_el.text.strip()
                href = title_el['href']
                print(f'Дата: {date}. Название статьи: {title}. Ссылка: {href}')


soup_scrapping()
