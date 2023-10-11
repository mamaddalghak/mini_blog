import asyncio
import aiomysql
async def show_comments(your_str):
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
    post = int(your_str[cursor2 + 2:cursor3])
    await test_example_execute(post)


async def test_example_execute(post):
    conn = await aiomysql.connect(host='localhost', port=3306,
                                    user='root', password='123456',
                                    db='mmd')

    cur = await conn.cursor()
    sql_statement = """
        SELECT * FROM comments WHERE id = %s;
    """
    values = (post)
    await cur.execute(sql_statement, values)
    result = await cur.fetchall()
    await cur.close()
    await conn.commit()
    for i in result:
        print(i[1] + " : " + i[0])
    conn.close()