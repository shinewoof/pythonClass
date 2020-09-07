import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin


class ＷebCrawler():

    def urlCrawler(self, domainList):
        newDomainList = []
        for domain in domainList:
            resp = requests.get(domain)
            soup = BeautifulSoup(resp.text, 'html.parser')
            all_a_tag = soup.find_all('a')

            for a_tag in all_a_tag:
                aTagUrl = urljoin(domain, a_tag.get("href"))
                newDomainList.append(aTagUrl)
                print(aTagUrl)

        return newDomainList



if __name__ == "__main__":

    inputParams = sys.argv
    domainList = [inputParams[1]]
    count = int(inputParams[2])

    runCount = 0

    while runCount < count:
        runCount += 1
        domainList = ＷebCrawler.urlCrawler([], domainList)
