import urllib.request as req
import bs4

url="https://www.theblockbeats.info/newsflash"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

request = req.Request(url, headers={
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
  data = response.read().decode("utf-8")
  
root = bs4.BeautifulSoup(data,"html.parser")

titles = root.find_all("a", class_="flash-item-title") 
print(titles)

contents = root.find_all("div", class_="flash-item-content") 
print(contents)
