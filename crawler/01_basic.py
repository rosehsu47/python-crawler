import urllib.request as req
url="https://www.ptt.cc/bbs/DigiCurrency/index.html"

requset=req.Request(url, headers={
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

with req.urlopen(requset) as response:
  data=response.read().decode("utf-8")

# print(data)

# 以下需要使用 beautifulsoup4
# python3 -m pip install beautifulsoup4

import bs4
root=bs4.BeautifulSoup(data,"html.parser")

print(root.title) # <title>看板 DigiCurrency 文章列表 - 批踢踢實業坊</title>
print(root.title.string) # 看板 DigiCurrency 文章列表 - 批踢踢實業坊

# 尋找 class="title" 的 div 標籤
titles=root.find("div", class_="title") 

print(titles)
# 結果：
# <div class="title">
# <a href="/bbs/DigiCurrency/M.1668343836.A.ABC.html">[閒聊] AAX也要跑路了嗎?</a>
# </div>

# 取出 titles a tag 的文字
print(titles.a.string) 
# 結果：
# [閒聊] AAX也要跑路了嗎?

titles=root.find_all("div", class_="title") 
for title in titles:  
  if title.a != None:
      print(title.a.string)