import passwordgenerator as passwordgenerator
import praw
import config
import time
import os





class Bot:
    def __init__(self, botname, redditor, cusername, cpassword, cclient_id, cclient_secret, subreddit = "", replystr = "", welcomestr = "", keywords = []):
        self.r = self.login(botname, redditor, cusername, cpassword, cclient_id, cclient_secret)
        self.keywords = keywords
        self.replystr = replystr
        self.welcomestr = welcomestr
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

    def task_reply(self):
        print("Searching last 1,000 comments")
        if bool(self.keywords) and self.replystr and self.subreddit:
            for comment in self.r.subreddit(self.subreddit).comments(limit=10000):
                res = [keyword for keyword in self.keywords if (keyword in comment.body)]
                if bool(res) and comment.author != self.r.user.me():
                    comment.refresh()
                    if self.r.user.me().name not in [x.author.name for x in comment.replies]:
                        print("my name is " + self.r.user.me().name)
                        print([x.author.name for x in comment.replies])
                        comment.reply(self.replystr)
                        print("Replied to comment " + comment.id)

            print("Search Completed.")

    def task_firstComment(self):
        print("Searching last 100 posts...")
        for submission in self.r.subreddit(self.subreddit).new(limit=100):
            print("New post!")
            if self.r.user.me().name not in [x.author.name for x in submission.comments]:
                print("commenting...")
                submission.reply(self.welcomestr)
                print("commented")


bot = Bot("testbot1", "tsaaaaaaaa", "tsaaaaaaaa", "parola123", "23bQR7XTzbODBmXw2WQHlg", "Qm8T8hV2SjHmdQGUYk6gKz5NZbT19w", subreddit= "tsaa", replystr= "cum sterg",welcomestr= "Tsaa! What a great post!", keywords= ["I like your dfs!"])

while True:
    bot.task_firstComment()
    bot.task_reply()
    time.sleep(10)
    print("Sleeping for 10 seconds....")
