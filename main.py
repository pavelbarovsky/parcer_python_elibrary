from bs4 import BeautifulSoup
import requests

# Получаем HTML-код страницы
url = 'http://127.0.0.1:52377/lipko_elib.html'
page = requests.get(url)
print(page.status_code) # если 200, то подключение успешно

# Создаем объект BeautifulSoup и находим таблицу по тегу 'table'
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', id='restab')

# создаем список названий статей
headers = []
for tr in table.find_all('tr'):
    titles = []
    for span in tr.find_all('span'):
        titles.append(span.text.strip())
    if titles:
        headers.append(titles)
headers.pop(0) # удаление лишнего элемента "Цит"

# создаем список имен авторов
Name_DATA = []
for tr in table.find_all('tr'):
    Name_data = []
    for i in tr.find_all('i'):
        Name_data.append(i.text.strip())
    if Name_data:
        Name_DATA.append(Name_data)

# Создаем список названий книг
book = []
for tr in table.find_all('tr'):
    collection_data = []
    for td in tr.find_all('td'):
        for font in td.find_all('font'):
            collection_data.append(font.text.strip())
        if collection_data:
            book.append(collection_data)

# убрать 3 лишних элемента списка
book.pop(0)
book.pop(0)
book.pop(0)
j=0
while j < len(book):
    # убрать в списке элемент с номером публикации
    del book[j][0]
    # убрать 2 повторяющихся элемента списка
    del book[j]
    del book[j]
    # убрать имя из элемента списка
    del book[j][0]
    j=j+1

# Выводим результаты
print(headers)
print(Name_DATA)
print(book)