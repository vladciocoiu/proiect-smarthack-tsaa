import passwordgenerator as passwordgenerator
import praw
import config
import time
import os





class Bot:
    def __init__(self, keywords, replystr, botname, redditor, cusername, cpassword, cclient_id, cclient_secret, subreddit):
        self.r = self.login(botname, redditor, cusername, cpassword, cclient_id, cclient_secret)
        self.keywords = keywords
        self.replystr = replystr
        self.subreddit = subreddit

    def login(self, botname, redditor, cusername, cpassword, cclient_id, cclient_secret):
        print("Logging in...")
        r = praw.Reddit(username=cusername,
                        password=cpassword,
                        client_id=cclient_id,
                        client_secret=cclient_secret,
                        user_agent=botname + " v1.0 by u/" + redditor)
        print("Logged in!")

        return r

    def run(self):
        print("Searching last 1,000 comments")

        for comment in self.r.subreddit(self.subreddit).comments(limit=10000):
            res = [keyword for keyword in self.keywords if (keyword in comment.body)]
            if bool(res) and comment.author != self.r.user.me():
                comment.refresh()
                if self.r.user.me().name not in [x.author.name for x in comment.replies.list()]:
                    print("my name is " + self.r.user.me().name)
                    print(comment.replies.list())
                    print([x.author.name for x in comment.replies])
                    comment.reply(self.replystr)
                    print("Replied to comment " + comment.id)

        print("Search Completed.")

        print("Sleeping for 10 seconds...")
        # Sleep for 10 seconds...
        time.sleep(10)


bot = Bot(["dfs"], "I like your dfs!", "testbot1", "tsaaaaaaaa", "tsaaaaaaaa", "parola123", "23bQR7XTzbODBmXw2WQHlg", "Qm8T8hV2SjHmdQGUYk6gKz5NZbT19w", "tsaa")

while True:
    bot.run()
