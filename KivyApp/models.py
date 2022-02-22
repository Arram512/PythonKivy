import os


def get_introductions():
    lessons_a = {}
    path = os.path.dirname(os.path.abspath(__file__))
    dir = "\\Images\\Intro\\"
    gifs = os.listdir(path + dir)
    for i in range(len(gifs)):
        gif = gifs[i].split('.')[0]
        lessons_a[path + dir + gifs[i]] = f"{gif}"

    return lessons_a

#print(get_lessons())
