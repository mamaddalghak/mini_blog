from human import human
from post import post
from like import like
from comment import comment
dicta = dict([])
posts = []
while True:
    z = str(input())
    i = 0
    while z[i] ==" ":
        i = i + 1
    r = i
    if z[r:r + 2] == "sp":
        i = i + 2
        y = z[i:len(z)]
        print(dicta[y].posts)
    elif z[r:r + 2] == "sc":
        i = i + 2
        y = z[i:len(z)]
        for j in posts:
            if j.text == y:
                print(j.comments)
    elif z[r:r + 2] == "p:":
        i = i + 2
        o = i
        while z[i:i + 2] != "n:":
            i = i + 1
        x = z[o:i]
        y = z[i + 2:len(z)]
        if y not in dicta.keys():
            dicta[y] = human(y, [x])
        else:
            dicta[y].posts.append(x)
        posts.append(post(x, y, {}))
    elif z[r:r + 2] == "l:":
        pass
    elif z[r:r + 2] == "c:":
        i = i + 2
        o = i
        while z[i:i + 2] != "n:":
            i = i + 1
        c = z[o:i]
        i = i + 2
        o = i
        while z[i:i + 2] != "p:":
            i = i + 1
        y = z[o:i]
        x = z[i + 2:len(z)]
        for j in posts:
            if j.text == x:
                j.comments[y] = c