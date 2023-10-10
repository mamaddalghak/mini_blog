def show_post(your_str, dictionari):
    tah = False
    cursor = 0
    while your_str[cursor] == " ":
        cursor = cursor + 1
    cursor2 = cursor
    for cursor in range(cursor, len(your_str)):
        if your_str[cursor] == " " and tah == False:
            cursor3 = cursor
            tah = True
        elif your_str[cursor] != " ":
            tah = False
        cursor = cursor + 1
    name = your_str[cursor2 + 2:cursor3]
    print(dictionari[name].posts)