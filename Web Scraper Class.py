#Scraper Class

class HouseScraper():
    headers = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding" : "gzip, deflate, br",
    "accept-language" : "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cache-control" : "max-age=0",
    "cookie" : "zguid=23|%24b4ab2df0-3bb3-44ac-a981-89b62daa7fc4; zgsession=1|aa2c1bc9-221c-42f8-9859-a5d81b022eb4; JSESSIONID=5895583B033EEF332472C82DEE9B70B2; AWSALB=suPHp9uUD3gAqtTrIL5gKua+XpLfpop9xujH1akhjiGgkG/QPpfxq9Ixj6u+QpjuzcmQuAq3+Jd4ERskwGx2MBqZMzPdtGKJJNsnn51TdPrCI58Uhesx8sark2e+; AWSALBCORS=suPHp9uUD3gAqtTrIL5gKua+XpLfpop9xujH1akhjiGgkG/QPpfxq9Ixj6u+QpjuzcmQuAq3+Jd4ERskwGx2MBqZMzPdtGKJJNsnn51TdPrCI58Uhesx8sark2e+; search=6|1618098527958%7Crect%3D45.74788083645929%252C-122.07473755116189%252C45.36227732844171%252C-123.31665044883812%26rid%3D13373%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0913373%09%09%09%09%09%09",
    "dnt" : "1",
    "referer" : "https://www.zillow.com/portland-or/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22portland%22%2C%22mapBounds%22%3A%7B%22west%22%3A-123.31665044883812%2C%22east%22%3A-122.07473755116189%2C%22south%22%3A45.36549357894722%2C%22north%22%3A45.744686397426456%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13373%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D",
    "sec-fetch-dest" : "document",
    "sec-fetch-mode" : "navigate",
    "sec-fetch-site" : "same-origin",
    "sec-fetch-user" : "?1",
    "upgrade-insecure-requests" : "1",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"                          
}
    
    def fetch(self, url, params):
        response = req.get(url, headers = self.headers, params = params)
        print(response)
        return response
    
    def parse(self, response):
        soup = bs(response.content, 'html.parser')
        print(soup)
        
    def run(self):
        url = "https://www.zillow.com/homes/portland_rb/"
        params = {
    "searchQueryState" : '{"pagination":{"currentPage": 1},"usersSearchTerm":"portland","mapBounds":{"west":-123.93852236914063,"east":-121.45286563085938,"south":45.357452602478155,"north":45.75267215956587},"regionSelection":[{"regionId":13373,"regionType":6}],"isMapVisible":true,"filterState":{"ah":{"value":true}},"isListVisible":true}'
}
        webpage = self.fetch(url, params)
        self.parse(webpage)
    
    
    
if __name__ == '__main__':
    scraper = HouseScraper()
    scraper.run()