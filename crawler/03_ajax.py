import urllib.request as req
url="https://medium.com/"

requset=req.Request(url, headers={
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

with req.urlopen(requset) as response:
  data=response.read().decode("utf-8")

# 使用內建套件 json
import json
data = json.loads(data)