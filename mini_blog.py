from human import human
from post import post
from like import like
from comment import comment
dicta = dict([])
posts = []
while True:
    tah = False
    z = str(input()) + " "
    i = 0
    while z[i] ==" ":
        i = i + 1
    r = i
    if z[r:r + 2] == "sp":
        z = str(input()) + " "
        i = 0
        while z[i] == " ":
            i = i + 1
        r = i
        while i < len(z):
            if z[i] == " " and tah == False:
                o = i
                tah = True
            elif z[i] != " ":
                tah = False
            i = i + 1
        y = z[r + 2:o]
        print(dicta[y].posts)
    elif z[r:r + 2] == "sc":
        z = str(input()) + " "
        i = 0
        while z[i] == " ":
            i = i + 1
        r = i
        while i < len(z):
            if z[i] == " " and tah == False:
                o = i
                tah = True
            elif z[i] != " ":
                tah = False
            i = i + 1
        y = z[r + 2:o]
        for j in posts:
            if j.text == y:
                print(j.comments)
    elif z[r:r + 2] == "p:":
        while i < len(z):
            if z[i] == " " and tah == False:
                o = i
                tah = True
            elif z[i] != " ":
                tah = False
            i = i + 1
        x = z[r + 2:o]
        z = str(input()) + " "
        i = 0
        while z[i:i + 2] != "n:":
            i = i + 1
        r = i
        tah = False
        while i < len(z):
            if z[i] == " " and tah == False:
                o = i
                tah = True
            elif z[i] != " ":
                tah = False
            i = i + 1
        y = z[r + 2:o]
        if y not in dicta.keys():
            print(x)
            dicta[y] = human(y, [x])
        else:
            print(x)
            dicta[y].posts.append(x)
        posts.append(post(x, y, {}))
    elif z[r:r + 2] == "l:":
        pass
    elif z[r:r + 2] == "c:":
        while i < len(z):
            if z[i] == " " and tah == False:
                o = i
                tah = True
            elif z[i] != " ":
                tah = False
            i = i + 1
        c = z[r + 2:o]
        z = str(input()) + " "
        i = 0
        while z[i] == " ":
            i = i + 1
        r = i
        while i < len(z):
            if z[i] == " " and tah == False:
                o = i
                tah = True
            elif z[i] != " ":
                tah = False
            i = i + 1
        y = z[r + 2:o]
        z = str(input()) + " "
        i = 0
        while z[i] == " ":
            i = i + 1
        r = i
        while i < len(z):
            if z[i] == " " and tah == False:
                o = i
                tah = True
            elif z[i] != " ":
                tah = False
            i = i + 1
        x = z[r + 2:o]
        for j in posts:
            if j.text == x:
                j.comments[y] = c
