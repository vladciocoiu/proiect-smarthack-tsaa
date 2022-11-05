import passwordgenerator as passwordgenerator
import praw
import config
import time
import os

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="The Reddit Commenter v1.0")
    print("Logged in!")

    return r


def run_bot(r, comments_replied_to):
    print("Searching last 1,000 comments")

    for comment in r.subreddit('tsaa').comments(limit=10000):
        if "dfs" in comment.body.lower() and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("String with \"test\" found in comment " + comment.id)
            if( r.user.me().name not in [x.author.name for x in comment.replies.list()] ):
                print("my name is " + r.user.me().name)
                print(comment.replies.list())
                print([x.author.name for x in comment.replies])
                comment.reply("Hey, I like your dfs!")
                print("Replied to comment " + comment.id)

            with open("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print("Search Completed.")

    print(comments_replied_to)

    print("Sleeping for 10 seconds...")
    # Sleep for 10 seconds...
    time.sleep(10)


comments_replied_to = []
r = bot_login()
print(comments_replied_to)

while True:
    run_bot(r, comments_replied_to)
