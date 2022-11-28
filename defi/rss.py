
import xml.etree.ElementTree as ET

# Using this python script to extract the Feed title and Feed URL from RAW.opml to pure text. Put the RAW.opml in the same directory.

# parse .opml to text
tree = ET.parse('RAW.opml')
root = tree.getroot()

source_list = []

if __name__ == '__main__':
    for child in root[1]:
        print(child.attrib['title'])
        for child2 in child:
            # print("\t"+child2.attrib['title']+': '+child2.attrib['xmlUrl'])
        
          source = {
            "category": child.attrib['title'],
            "rss_title": child2.attrib['title'],
            "rss_url":  child2.attrib['xmlUrl'],
          }
          source_list.append(source)

# parse feed
import feedparser

print("source_list: ", len(source_list))

for source in source_list:
  # print(feedparser.parse("https://nakamoto.com/rss/").keys())

  feed = feedparser.parse(source["rss_url"])
  print(len(feed.entries))

  for entry in feed.entries:
    print(entry.title)
    print(entry.link)

    s = entry.description
    # description
    # print(s.replace('&nbsp;','').replace('&#039;','')) # code 4
    # print(s.split('<br />')[0].replace('&nbsp;','').replace('&#039;','')) # code 4
    # print(s.split('<br />')[1].replace('&nbsp;','').replace('&#039;',''))  # code 5 
   
    print(entry.description)
    # print(entry.published_parsed)


    # data = entry.description
    # import bs4
    # root=bs4.BeautifulSoup(data,"html.parser")

    # print(root.p.string) 