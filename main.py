import json
from db_config import create, insert_into_db
from parser import parser
import re
from pprint import pprint
import time
from datetime import datetime
from utils import read_files_zip

DIR_PATH = r"C:\Users\beerva.joshi\PycharmProjects\products\toters_3680_-15753_-62974_1.html.gz"
TABLE_NAME = 'Products'

def main():
    create(TABLE_NAME)
    raw_data = read_files_zip(DIR_PATH)
    result = parser(raw_data)
    print(type(result))
    insert_into_db(table_name=TABLE_NAME, data=result)


if __name__ == '__main__':
    st = time.time()
    main()
    tt = time.time() - st
    print(tt)