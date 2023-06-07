import os

from browser import browser
from reader import Reader

from config import DEBUG_PATH


def chechFolders():
    if not os.path.exists(DEBUG_PATH):
        os.mkdir(DEBUG_PATH)


if __name__ == '__main__':
    try:
        chechFolders()

        reader = Reader()
        reader.write_article_output()

        browser.close()
    except Exception as e:
        print(e)

        if browser is not None:
            browser.close()
