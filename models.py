from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
task_list = client[Config.DATABASE]
task = ['this_is_a_test']

