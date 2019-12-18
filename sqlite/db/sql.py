import sqlite3
from sqlite3 import Error

# SQLiteデータベースへのデータベース接続を作成します
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect('example.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r'C:\sqlite\db\pythonsqlite.db')
'''
c.execute() # 実行

conn.commit() # セーブ

conn.close()　# 閉じる
'''