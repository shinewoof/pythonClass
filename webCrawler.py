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
        """
        34 行 ＷebCrawler.urlCrawler([], domainList) 雖然 work，但實務上不會這樣寫

        我們可以有２個做法：
        1. 確實地 instantiation ＷebCrawler 後再呼叫該 instance 的 method 來用
            e.g.
                    
                wc = ＷebCrawler()
                domainList = wc.urlCrawler(domainList)
        

        2. 若希望 ＷebCrawler 只是當作一個 namespace，那麼可以將 urlCrawler 改成 "staticmethod"
            使用 @staticmethod 的修飾器來達成，此時就不需要 self 參數指向自己
            e.g.

                class ＷebCrawler():
                    
                    @staticmethod
                    def urlCrawler(domainList):
                        ...

            34 行就可改寫成：

                domainList = ＷebCrawler.urlCrawler(domainList)

            可參考文章了解更多： https://realpython.com/instance-class-and-static-methods-demystified/
        """
        