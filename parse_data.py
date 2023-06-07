from config import URL_PARENT
from config import URL_SEARCH, URL_SEARCH_DATA
from config import URL_SEARCH_AUTHORS, URL_SEARCH_AUTHOR_DATA
from config import URL_AUTHOR_PROFILE

from browser import browser, browser_get, set_data_form, pause_on_loading_page
from parse_html import search_id_autor, search_index_hirsha, search_article, search_article_data


def __parse_author_id(search_name: str) -> str | None:
    autor_data: dict = URL_SEARCH_AUTHOR_DATA.copy()
    autor_data['surname'] = search_name

    browser_get(URL_SEARCH_AUTHORS)

    set_data_form(data=autor_data)

    browser.execute_script("author_search();")
    pause_on_loading_page()

    with open('./debug/3. author_search.html', 'w', encoding="utf8") as f:
        f.write(browser.page_source)

    return search_id_autor(browser.page_source)


def parse_hirshi(search_name: str) -> dict[str, str] | None:
    author_id: str | None = __parse_author_id(search_name=search_name)

    if author_id is None:
        print('Не найден Id автора')
        return

    browser_get(URL_AUTHOR_PROFILE.format(author_id=author_id))
    pause_on_loading_page()

    with open('./debug/4. author_profile.html', 'w', encoding="utf8") as f:
        f.write(browser.page_source)

    index_hirsha: str | None = search_index_hirsha(browser.page_source)

    if index_hirsha is None:
        print('Не найден Индекс Хирша')
        return

    return {
        "user_name": search_name,
        "index_hirsha": index_hirsha
    }


def parse_article(search_name: str):
    article_data: dict = URL_SEARCH_DATA.copy()
    article_data['ftext'] = search_name

    browser_get(URL_SEARCH)

    set_data_form(data=article_data)

    browser.execute_script("query_message();")
    pause_on_loading_page()

    with open('./debug/1. article_search.html', 'w', encoding="utf8") as f:
        f.write(browser.page_source)

    url = search_article(browser.page_source)

    if url is None:
        print(search_name + ' = Не найдена ссылка')
        return

    article_data: dict = __parse_article_data(url)
    article_data['article_name'] = search_name

    return article_data


def __parse_article_data(article_url: str):
    browser_get(URL_PARENT + article_url)

    with open('./debug/2. article_profile.html', 'w', encoding="utf8") as f:
        f.write(browser.page_source)

    return search_article_data(browser.page_source)
