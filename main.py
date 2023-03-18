from bs4 import BeautifulSoup
import requests


# в качестве параметра функции передаём string с ссылкой
def ElibParcer(url):
    page = requests.get(url)
    print(page.status_code) # если 200, то подключение успешно
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', id='restab')

    # создаем список названий статей
    titles = []
    for tr in table.find_all('tr'):
        headers = []
        for span in tr.find_all('span'):
            headers.append(span.text.strip())
        if headers:
            titles.append(headers)
    # удаление лишнего элемента "Цит"
    titles.pop(0)

    # создаем список имен авторов
    authors = []
    for tr in table.find_all('tr'):
        name_data = []
        for i in tr.find_all('i'):
            name_data.append(i.text.strip())
        if name_data:
            authors.append(name_data)

    # Создаем список названий книг
    book_titles = []
    for tr in table.find_all('tr'):
        book_data = []
        for td in tr.find_all('td'):
            for font in td.find_all('font'):
                book_data.append(font.text.strip())
            if book_data:
                book_titles.append(book_data)

    # убрать 3 лишних элемента списка
    book_titles.pop(0)
    book_titles.pop(0)
    book_titles.pop(0)
    j = 0
    while j < len(book_titles):
        # убрать в списке элемент с номером публикации
        del book_titles[j][0]
        # убрать 2 повторяющихся элемента списка
        del book_titles[j]
        del book_titles[j]
        # убрать имя из элемента списка
        del book_titles[j][0]
        j = j + 1

    # Выводим результаты
    print(titles)
    print(authors)
    print(book_titles)


ElibParcer('http://127.0.0.1:60107/lipko_elib.html')


