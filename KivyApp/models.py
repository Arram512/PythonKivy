import os
import sqlite3

def get_introductions(item):
    lessons_a = {}
    path = os.path.dirname(os.path.abspath(__file__))
    dir = f"\\Images\\{item}\\"
    gifs = os.listdir(path + dir)
    for i in range(len(gifs)):
        gif = gifs[i].split('.')[0]
        lessons_a[path + dir + gifs[i]] = f"{gif}"

    return lessons_a

# def get_description(item):
# 	pass

def query():
    db = sqlite3.connect('app.db')
    cursor = db.cursor()

    query = ""

    cursor.execute(query)
    db.commit()

