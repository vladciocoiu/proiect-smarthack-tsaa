
# {
#     "taskQueue":
#     [
#         {
#             "type": "find",
#             "keywords": ["keyword1", "keyword2"]
#         },
#         {
#             "type": "reply",
#             "keywords": ["keyword1", "keyword2"],
#             "message": "message2"
#         },
#         {
#             "type": "sendResults",
#             "time": "10M"
#         }
#     ]
# }

import json

class TaskQueue:
    def __init__(self, jsonTasks):
        #print("Json Tasks:", jsonTasks)
        self.tasks = jsonTasks
    def getTasks(self):
        return self.tasks
