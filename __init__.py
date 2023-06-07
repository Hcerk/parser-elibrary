from reader import Reader

from browser import browser

if __name__ == '__main__':
    try:
        reader = Reader()
        reader.write_article_output()

        browser.close()
    except Exception as e:
        print(e)

        if browser is not None:
            browser.close()
