import os
import json

from datetime import datetime

from config import INPUT_PATH_FILE, OUTPUT_PATH_FILE

from parse_data import parse_article, parse_hirshi


class Reader:
    articles_name: list[str] = []

    def __read_articles(self):
        if not os.path.isfile(INPUT_PATH_FILE):
            with open(INPUT_PATH_FILE, "w", encoding="utf8") as f:
                f.write("")
        else:
            with open(INPUT_PATH_FILE, "r", encoding="utf8") as f:
                for article in f.read().split("\n"):
                    if article.lower().strip() != "":
                        self.articles_name.append(article.strip())

    def write_article_output(self):
        self.__read_articles()

        articles: list[dict] = []

        for article_name in self.articles_name:
            article_data: dict = parse_article(search_name=article_name)

            articles.append(article_data)

        for article in articles:
            users: list[dict] = []

            if 'users_name' in article:
                for user_name in article['users_name']:
                    user_data: dict = parse_hirshi(search_name=user_name)

                    users.append(user_data)

            article['users'] = users

        resuilt_json = json.dumps(articles, indent=4)

        date_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(OUTPUT_PATH_FILE.format(date=date_string), "w", encoding="utf8") as f:
            f.write(resuilt_json)
