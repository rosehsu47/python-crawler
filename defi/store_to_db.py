import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS articles
  (title text, content text, url text PRIMARY KEY)''')

# cur.execute('''INSERT INTO articles VALUES 
#   ('article', 'content', 'url')''')

con.commit()


article =  ('1', '2', '3')

article_list = []
article_list.append(article)

cur.executemany("INSERT OR IGNORE INTO articles VALUES (?, ?, ?)", article_list)

for row in cur.execute('''SELECT * FROM articles'''):
  print(row)
