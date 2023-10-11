import asyncio
from Human import Human
from Post import Post
from Like import Like
from Comment import Comment
from show_post import show_post
from show_comments import show_comments
from post_function import post_function
from comment_function import comment_function
from create_post import add_post
from create_comment import add_comment

async def main():
    while True:
        your_str = str(input()) + " "
        cursor = 0
        while your_str[cursor] == " ":
            cursor = cursor + 1
        cursor2 = cursor
        if your_str[cursor2:cursor2 + 2] == "sp":
            your_str = str(input()) + " "
            await show_post(your_str)
        elif your_str[cursor2:cursor2 + 2] == "sc":
            your_str = str(input()) + " "
            await show_comments(your_str)
        elif your_str[cursor2:cursor2 + 2] == "p:":
            post = post_function(your_str)
            your_str = str(input()) + " "
            name = post_function(your_str)
            await add_post(post,name)
        elif your_str[cursor2:cursor2 + 2] == "l:":
            pass
        elif your_str[cursor2:cursor2 + 2] == "c:":
            comment = comment_function(your_str)
            your_str = str(input()) + " "
            name = comment_function(your_str)
            your_str = str(input()) + " "
            post = int(comment_function(your_str))
            await add_comment(comment,name,post)

if __name__ == '__main__':
    asyncio.run(main())