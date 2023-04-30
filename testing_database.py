import sqlite3

sqliteConnection = sqlite3.connect('articles.db')
cursor = sqliteConnection.cursor()
sqlite_select_query = """SELECT * from post;"""
cursor.execute(sqlite_select_query)
posts = cursor.fetchall()
cursor.close()

for post in posts:    
    print(posts)