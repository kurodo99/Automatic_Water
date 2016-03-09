import datetime
from pymongo import MongoClient

from Class.RedisDatabase import RedisDatabase


class Statistic:
    current_status = {}

    def __init__(self):
        self.redis_database = RedisDatabase()
        self.mongo_client = MongoClient()
        self.mongo_database = self.mongo_client["smart_aqua"]
        self.stat = self.mongo_database.statistic

    def update_data(self):
        # Water Level
        self.current_status[RedisDatabase.WATER_LEVEL] = self.redis_database.get_water_level()
        # Screen Mode
        if self.redis_database.get_screen_mode() is not None:
            self.current_status[RedisDatabase.SCREEN_MODE] = self.redis_database.get_screen_mode()
        else:
            self.current_status[RedisDatabase.SCREEN_MODE] = self.redis_database.get_screen_mode()

        # Date
        self.current_status["date"] = datetime.datetime.utcnow()

    def save(self):
        print(self.stat.insert_one(self.current_status).inserted_id)
        self.current_status = {}

    def update_and_save(self):
        self.update_data()
        self.save()
