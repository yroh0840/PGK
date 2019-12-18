import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute() # 実行

conn.commit() # セーブ

conn.close()　# 閉じる