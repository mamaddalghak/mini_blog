import asyncio
import aiomysql
async def add_post(text,name):
    await test_example_execute(text, name)

async def test_example_execute(text, name):
    conn = await aiomysql.connect(host='localhost', port=3306,
                                    user='root', password='123456',
                                    db='mmd')

    cur = await conn.cursor()
    number_of_rows = await cur.execute("SELECT * FROM posts")
    sql_statement = """
    INSERT INTO posts (id,the_text,user_name) VALUES (%s,%s,%s);
    """
    await conn.commit()
    values = (number_of_rows + 1, text, name)
    await cur.execute(sql_statement, values)
    await conn.commit()
    conn.close()