import time
import requests
import threading
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import queue


def urlCrawler(q):
    while q.qsize():
        domain = q.get()
        print(domain)
        t = threading.Thread(target=threadUrlCrawler, args=(domain, q))
        t.start()
    
    t.join()


def threadUrlCrawler(domain, q):
    resp = requests.get(domain)
    soup = BeautifulSoup(resp.text, 'html.parser')
    all_a_tag = soup.find_all('a')

    for a_tag in all_a_tag:
        aTagUrl = urljoin(domain, a_tag.get("href"))
        q.put(aTagUrl)
        print(aTagUrl)


if __name__ == "__main__":

    inputParams = sys.argv
    domain = inputParams[1]
    count = int(inputParams[2])
    q = queue.Queue()
    q.put(domain)
    runCount = 0

    while runCount < count:
        runCount += 1
        print(runCount)
        urlCrawler(q)
