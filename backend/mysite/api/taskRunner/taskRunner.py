from ..models import *
from ..redditwrapper.reddit import RedditBot
from .taskQueue import TaskQueue
import asyncio
import time

# class Bot(models.Model):
#     userId = models.IntegerField()
#     username = models.CharField(max_length=100)
#     active = models.BooleanField(default=False)
#     redditUsername = models.CharField(max_length=100)
#     clientId = models.CharField(max_length=100)
#     clientSecret = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     Task = models.JSONField(default=dict)


Bots = [
    Bot(
        0,
        userId = 1,
        username = "tsaaaaaaaa",
        active = True,
        redditUsername = "alin090402",
        clientId = "23bQR7XTzbODBmXw2WQHlg",
        clientSecret = "Qm8T8hV2SjHmdQGUYk6gKz5NZbT19w",
        password = "parola123",
        taskQueue = 
        [
            {
                "type": "find",
                "params": 
                {
                    "keywords": ["bug", "wrong", "buggy", "glitch"],
                    "subreddit": "FIFA",
                    "findIn": "posts"
                }
            },
            {
                "type": "notify",
                "params":
                {
                    "interval": 60
                }
            }


        ]

        
    ),
    Bot(
        1,
        userId = 1,
        username = "test2",
        active = False,
        redditUsername = "test2",
        clientId = "test2",
        clientSecret = "test2",
        password = "test2",
        taskQueue = {"Type": "reply", "params": {"subreddit": "test2", "keywords": ["test2"], "message": "test2"}}
    )

]


class BotRunner:
    def __init__(self, bot):
        self.bot = bot
        self.loggedIn = False
        #def __init__(self, redditor, botUsername, botPassword, botClientId, botClientSecret):
        self.redditBot = RedditBot(
                                    redditor=self.bot.redditUsername, 
                                    botUsername=self.bot.username, 
                                    botPassword=self.bot.password,
                                    botClientId=self.bot.clientId,
                                    botClientSecret=self.bot.clientSecret)



class taskRunner:
    def __init__(self):
        self.started = False
        self.redditWrapper = ()
        print("TaskRunner initialized")
    def start(self):
        self.started = True
    def stop(self):
        self.started = False
    def run(self):
        print("intra in run")
        botRunners = {}
        while(self.started):
            for bot in Bots:
                if(bot.active):
                    if(bot.id not in botRunners):
                        botRunners[bot.id] = BotRunner(bot)
                    botRunner = botRunners[bot.id]
                    if(not botRunner.loggedIn):
                        botRunner.redditBot.login()
                        botRunner.loggedIn = True
                    taskQ = TaskQueue(bot.taskQueue)
                    tasks = taskQ.getTasks()
                    results = []
                    #print("Running tasks for bot: ", tasks)
                    for task in tasks:
                        #print("Running task: ", task)
                        if(task["type"] == "find"):
                            results = botRunner.redditBot.task_find(task["params"]["keywords"], task["params"]["subreddit"], task["params"]["findIn"])
                        if(task["type"] == "reply"):
                            botRunner.redditBot.task_reply(results, task["params"]["message"])
                        if(task["type"] == "delete"):
                            botRunner.redditBot.task_delete(results)
                        if(task["type"] == "notify"):
                            botRunner.redditBot.task_notify(60)
                    time.sleep(3)




