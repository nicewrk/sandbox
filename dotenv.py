import os

def run():
    dotenv_strings = list()
    with open('.env') as f:
        dotenv_strings = f.readlines()

    for dotenv_string in dotenv_strings:
        try:
            line = dotenv_string.strip()
            k = line.split('=')[0]
            v = line.replace(k+'=','')
            os.environ.setdefault(k, v)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    run()
