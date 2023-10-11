import asyncio
import aiomysql
async def add_comment(text,name,id):
    await test_example_execute(text, name, id)

async def test_example_execute(text,name,id):
    conn = await aiomysql.connect(host='localhost', port=3306,
                                    user='root', password='123456',
                                    db='mmd')

    cur = await conn.cursor()
    sql_statement = """
    INSERT INTO comments (the_text,user_name,id) VALUES (%s,%s,%s);
    """
    await conn.commit()
    values = (text, name, id)
    await cur.execute(sql_statement, values)
    await conn.commit()
    conn.close()