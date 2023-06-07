## Парсер сайта elibrary

Парсер написанный для быстрого получение информации о статьи и получение значений Хирша у авторов данной статьи

Быстрый старт
-

- Скачать данный репозиторий
- Скачать Chrome Browser версии 113.0 и выше - [Скачать](https://www.google.com/intl/ru/chrome/)
- Скачать chromdriver [Скачать](https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.63/)
- Файл `chromdriver.exe` поместить в папку `browser`
- Установить Python 3.10.0 [Скачать Python](https://www.python.org/downloads/release/python-3100/)
- Перейти в корень проека и установить необходимые библеотеки ```py -m pip install -r requirements.txt```
- Прописать файл с наименованиями статей в папку `input` -> файл `articles.txt`

Итоговый результат
-
Итоговый результат будет лежать в папке `output` в файле `result-{date}.json`, где date - дата создания файла