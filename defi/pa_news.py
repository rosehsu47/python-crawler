import urllib.request as req

#TagId hebobp 交易所
url="https://www.panewslab.com/webapi/sqtopic/day?TagId=hebobp&LId=1&BeginTime=1667232000&EndTime=1669823999&Rn=200&tw=0"

request = req.Request(url, headers={

})

with req.urlopen(request) as response:
  data = response.read().decode("utf-8")

import json 
data = json.loads(data)
posts = data["data"]["calendars"]
# print(posts)

import bs4

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

for post in posts:
  print(post["title"])
  print(post["url"])

  url = post["url"]

  requset=req.Request(url, headers={
    "User-Agent": user_agent
  })

  with req.urlopen(requset) as response:
    data=response.read().decode("utf-8")

  root = bs4.BeautifulSoup(data,"html.parser")

  content = root.find("div", id="txtinfo") 
  # print(content.find_all("p"))
  for p_content in content.find_all("p"):
    print(p_content.string)
