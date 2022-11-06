import praw
import time
import os





class RedditBot:
    def __init__(self, redditor, botUsername, botPassword, botClientId, botClientSecret):
        self.redditor = redditor
        self.botUsername = botUsername
        self.botPassword = botPassword
        self.botClientId = botClientId
        self.botClientSecret = botClientSecret
        self.stats = {"replyCount": 0, "deleteCount": 0, "lastRun": time.time(), "keywords": {}, "wrongTitles": []}
        self.redditor = redditor

    def login(self):
        self.r = praw.Reddit(username=self.botUsername,
                        password=self.botPassword,
                        client_id=self.botClientId,
                        client_secret=self.botClientSecret,
                        user_agent=self.botUsername + " v1.0 by u/" + self.redditor)
        print("Logged in!")

    def task_find(self, keywords, subreddit, findIn):
        print("find task started")
        print("keywords: ", keywords, "subreddit: ", subreddit, "findIn: ", findIn)
        if not bool(keywords) or not bool(subreddit) or not bool(findIn):
            return "Error: Missing parameters"
        answer = []
        print("params ok")
        if findIn == "comments":
            for comment in self.r.subreddit(subreddit).comments(limit=10000):
                #print("comment found:", comment.body)
                res = [keyword for keyword in keywords if (keyword in comment.body)]
                if bool(res) and comment.author != self.r.user.me():
                    comment.refresh()
                    if self.r.user.me().name not in [x.author.name for x in comment.replies]:
                        #print("comment added:", comment.body)
                        for keyword in res:
                            if keyword not in self.stats["keywords"]:
                                self.stats["keywords"][keyword] = 1
                            else:
                                self.stats["keywords"][keyword] += 1
                        answer.append(comment)
        elif findIn == "posts":
            for submission in self.r.subreddit(subreddit).new(limit=100):
                res = [keyword for keyword in keywords if (keyword in submission.title)]
                if bool(res) and self.botUsername not in [x.author.name for x in submission.comments if x.author]:
                    answer.append(submission)
                    if submission.title not in self.stats["wrongTitles"]:
                        self.stats["wrongTitles"].append(submission.title)
                    for keyword in res:
                            if keyword not in self.stats["keywords"]:
                                self.stats["keywords"][keyword] = 1
                            else:
                                self.stats["keywords"][keyword] += 1
        print("find task finished, answer=", answer)
        return answer

    def task_reply(self, commentList, message):
        print("reply task started")
        if not bool(commentList) or not bool(message):
            return "Error: Missing parameters"
        for comment in commentList:
            print("reply status code: ", comment.reply(message))
            self.stats["replyCount"] += 1
        print("reply task finished")

    def task_delete(self, commentList):
        print("delete task started")
        if not bool(commentList):
            return "Error: Missing parameters"
        print("delete commentList: ", commentList)
        for comment in commentList:
            print("deleting ", comment , " delete status code: ", comment.mod.remove())
            self.stats["deleteCount"] += 1
        comment = self.r.comment("iv8oafx")
        print("comment: ", comment)
        comment.mod.remove()

        print("delete task finished")
    
    def task_notify(self, timeInterval):
        print("notify task started")
        print("timePassed: ", time.time() - self.stats["lastRun"])
        if time.time() - self.stats["lastRun"] < timeInterval:
            return False
        print("enough time has passed")
        messageSent = "Statistics for " + self.r.user.me().name + ":                            \n"
        messageSent += "Replied to " + str(self.stats["replyCount"]) + " comments               \n"
        messageSent += "Deleted " + str(self.stats["deleteCount"]) + " comments                 \n"
        messageSent += "Last run: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.stats["lastRun"]))
        messageSent += "\n\nKeywords:                           \n"
        
        for keyword in self.stats["keywords"]:
            messageSent += keyword + ": " + str(self.stats["keywords"][keyword]) + "\n"

        if len(self.stats["wrongTitles"]) > 0:
            messageSent += "Wrong titles:                        \n"
            for title in self.stats["wrongTitles"]:
                messageSent += title + "                         \n"
        
        print("messageSent: ", messageSent)
        print("redditor: ", self.r.redditor(self.redditor))
        print("status", self.r.redditor(self.redditor).message(subject="Statistics",message=messageSent))
        
        self.stats["lastRun"] = time.time()
        self.stats["replyCount"] = 0
        self.stats["deleteCount"] = 0
        self.stats["keywords"] = {}
        self.stats["wrongTitles"] = []
       
        print("notify task finished")
        return True



    # def task_reply(self):
    #     print("Searching last 1,000 comments")
    #     if bool(self.keywords) and self.replystr and self.subreddit:
    #         for comment in self.r.subreddit(self.subreddit).comments(limit=10000):
    #             res = [keyword for keyword in self.keywords if (keyword in comment.body)]
    #             if bool(res) and comment.author != self.r.user.me():
    #                 comment.refresh()
    #                 if self.r.user.me().name not in [x.author.name for x in comment.replies]:
    #                     print("my name is " + self.r.user.me().name)
    #                     print([x.author.name for x in comment.replies])
    #                     comment.reply(self.replystr)
    #                     print("Replied to comment " + comment.id)

    #         print("Search Completed.")

    # def task_firstComment(self):
    #     print("Searching last 100 posts...")
    #     for submission in self.r.subreddit(self.subreddit).new(limit=100):
    #         print("New post!")
    #         if self.r.user.me().name not in [x.author.name for x in submission.comments]:
    #             print("commenting...")
    #             submission.reply(self.welcomestr)
    #             print("commented")


#bot = RedditBot("testbot1", "tsaaaaaaaa", "tsaaaaaaaa", "parola123", "23bQR7XTzbODBmXw2WQHlg", "Qm8T8hV2SjHmdQGUYk6gKz5NZbT19w", subreddit= "tsaa", replystr= "cum sterg",welcomestr= "Tsaa! What a great post!", keywords= ["I like your dfs!"])
