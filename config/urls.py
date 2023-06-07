URL_PARENT: str = 'https://elibrary.ru'

URL_SEARCH: str = URL_PARENT + '/querybox.asp'
URL_SEARCH_DATA: dict = {
    'where_name': True,
    'type_article': True,
    'issues': 'all',
    'order': 'rev'
}

URL_SEARCH_AUTHORS: str = URL_PARENT + '/authors.asp'
URL_SEARCH_AUTHOR_DATA: dict = {
    'metrics': '1',
    'sortorder': '0',
    'order': '0',
    'orgid': '20179',
    'orgname': 'Уфимский университет науки и технологий',
    'town': 'Уфа',
    'countryid': 'RUS'
}

URL_AUTHOR_PROFILE = URL_PARENT + '/author_profile.asp?authorid={author_id}'
