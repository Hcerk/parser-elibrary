from bs4 import BeautifulSoup, ResultSet

import re


def search_id_autor(html: str) -> str | None:
    """
        Получаем Id автора.
    """

    # with open('./example/example2.html', 'r', encoding="utf8") as f:
    #     soup = BeautifulSoup(f.read(), 'html.parser')

    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')

    tables: ResultSet = soup.find_all('table')

    table: BeautifulSoup
    for table in reversed(tables):
        if 'Хирш' in table.text:
            trs: ResultSet = table.find_all('tr')

            tr: BeautifulSoup

            for tr in trs:
                if 'id' in tr.attrs:
                    return re.findall(r'(\d+)', tr['id'])[0]
            break

    '''
        Если не нашёлся id, кидаем нулевой объект
    '''

    return None


def search_index_hirsha(html: str) -> str | None:
    """
        Получаем Индекс Хирша в профиле автора.
    """

    # with open('./example/example2_profile.html', 'r', encoding="utf8") as f:
    #     soup = BeautifulSoup(f.read(), 'html.parser')

    soup = BeautifulSoup(html, 'html.parser')

    tables: ResultSet = soup.find_all('table')

    table: BeautifulSoup
    for table in reversed(tables):
        if 'Название показателя' in table.text:
            trs: ResultSet = table.find_all('tr')

            tr: BeautifulSoup
            for tr in trs:
                title = tr.find('font', {'color': '#00008f'})

                if title is None:
                    continue

                title_text: str = re.sub(r'\s+', ' ', title.text)

                if 'Индекс Хирша без учета самоцитирований' in title_text:
                    value_hirshi: BeautifulSoup = tr.find('font', {'color': '#000000'})
                    value_hirshi: str = value_hirshi.text

                    return value_hirshi
            break

    '''
        Если не нашёлся Индекс Хирша, кидаем нулевой объект
    '''
    return None


def search_article(html: str) -> str | None:
    """
        Получение ссылки на статью
    """

    # with open('./example/search_articles.html', 'r', encoding="utf8") as f:
    #     soup = BeautifulSoup(f.read(), 'html.parser')

    soup = BeautifulSoup(html, 'html.parser')

    table: BeautifulSoup = soup.find('table', {'id': 'restab'})

    if table is None:
        raise Exception("ъОшибка в парсинге")

    links: ResultSet = table.find_all('a')

    link: BeautifulSoup
    for link in links:
        if 'href' in link.attrs:
            if 'item' in link.attrs['href']:
                return link.attrs['href']

    return None


def __search_article_users(soup: BeautifulSoup) -> list[str]:
    """
        Получаем авторов у статьи
    """

    users = []

    # with open('./example/article.html', 'r', encoding="utf8") as f:
    #     soup = BeautifulSoup(f.read(), 'html.parser')

    divs: ResultSet = soup.find_all('div')

    div: BeautifulSoup
    for div in reversed(divs):
        img: BeautifulSoup = div.find('img')

        if img and 'src' in img.attrs and 'about_author.gif' in img.attrs['src']:
            font: BeautifulSoup = div.find('font', {'color': '#00008f'})

            if font.text.strip() not in users:
                users.append(font.text.strip())

    return users


def search_article_data(html: str):
    """
        Получаем "Импакт-фактор журнала в РИНЦ", "Норм. цитируемость по журналу" и пользователей
    """

    # with open('./debug/article.html', 'r', encoding="utf8") as f:
    #       soup = BeautifulSoup(f.read(), 'html.parser')

    soup = BeautifulSoup(html, 'html.parser')

    response = {
        'users_name': __search_article_users(soup=soup),
        'impact_factor_journal': '',
        'citation_journal': ''
    }

    tds: ResultSet = soup.find_all('td')

    td: BeautifulSoup
    for td in tds:
        img: BeautifulSoup = td.find('img')

        if img and 'src' in img.attrs and 'but_orange_question.gif' in img.attrs['src']:
            if 'Импакт-фактор журнала в РИНЦ' in td.text and 'Норм. цитируемость по журналу' in td.text:
                continue

            if 'Цитирований в РИНЦ' in td.text:
                font: BeautifulSoup = td.find('font')

                response['citation_in_rinc'] = font.text

            if 'Импакт-фактор журнала в РИНЦ' in td.text:
                font: BeautifulSoup = td.find('font')

                response['impact_factor_journal'] = font.text

            if 'Норм. цитируемость по журналу' in td.text:
                font: BeautifulSoup = td.find('font')

                response['citation_journal'] = font.text

    return response
