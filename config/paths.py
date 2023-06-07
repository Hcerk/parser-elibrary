import os

PARENT_PATH = os.path.dirname(os.path.abspath(__name__))

CHROME_DRIVER_EXE = PARENT_PATH + '\\browser\\chromedriver.exe'

INPUT_PATH = PARENT_PATH + '\\input'
OUTPUT_PATH = PARENT_PATH + '\\output'

INPUT_NAME_FILE = '\\articles.txt'
INPUT_PATH_FILE = INPUT_PATH + INPUT_NAME_FILE

OUTPUT_NAME_FILE = '\\result_{date}.json'
OUTPUT_PATH_FILE = OUTPUT_PATH + OUTPUT_NAME_FILE
