import os
import json
import gzip


def read_files(path: str):
    '''
    generator func that takes dir path as input param in string
    and iterates over files and yield results
    '''
    try:
        files = os.listdir(path)
        for file in files:
            filename = os.path.join(path, file)
            content = open(filename).read()
            yield json.loads(content)
    except Exception as e:
        print("Error in func:", read_files.__name__, '\nError: ', e)


def read_files_zip(path: str):
    try:
        with gzip.open(path,"rt",encoding="utf-8") as f:
            data=json.load(f)
        return data
    except Exception as e:
        print("Error in func:", read_files.__name__, '\nError: ', e)

if __name__ == '__main__':
    pass
