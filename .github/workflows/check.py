from datetime import datetime, timedelta
import requests
from pytz import timezone
from bs4 import BeautifulSoup
import os


def main():
    kst = timezone('Asia/Seoul')
    date = (datetime.now(kst) - timedelta(weeks=1)).strftime("%y%m%d")
    url = "https://github.com/weekday-algorithm-study/Algorithm-Study/tree/main/baekjoon/"
    record = [[], []]

    for num in range(1, 3):
        html = requests.get(url + str(date) + "/문제" + str(num)).content
        soup = BeautifulSoup(html, 'html.parser')

        infos = soup.find_all('a', attrs={'class': 'js-navigation-open Link--primary'})

        for info in infos:
            record[num - 1].append(info.get_text()[:-3])

    send(date, record)


def send(date, record):

    MESSAGE_URL = os.environ['MESSAGE_URL']

    message = {'content':
                   str(date) + " 문제 푼 사람" + "\n" +
                   "문제1: " + ', '.join(record[0]) + "\n" +
                   "문제2: " + ', '.join(record[1])
               }

    requests.post(MESSAGE_URL, data=message)


if __name__ == "__main__":
    main()
