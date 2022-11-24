import urllib.request as req

def getData(url):
  requset = req.Request(url, headers={
    # 帶上 Cookie
    "cookie": "over18=1",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
  })

  with req.urlopen(requset) as response:
    data = response.read().decode("utf-8")

  # print(data)

  # 以下需要使用 beautifulsoup4
  # python3 -m pip install beautifulsoup4

  import bs4
  root = bs4.BeautifulSoup(data,"html.parser")

  titles = root.find_all("div", class_="title") 
  for title in titles:  
    if title.a != None:
        print(title.a.string)
        continue

  # 抓取上一頁的連結
  nextLink = root.find("a",string="‹ 上頁")
  # print(nextLink)
  return nextLink["href"]

startPageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"

count = 0 
while count < 3:
  print("第", count+1, "頁")
  nextPageUrl = "https://www.ptt.cc"+getData(startPageUrl)
  # print(nextPageUrl)
  count+=1
