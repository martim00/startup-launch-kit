from pymongo import MongoClient


class Lunch:
    def __init__(self, app):
        self.app = app
        self.client = MongoClient()

    def register(self, collection):
        collection.configure_db(self.client.main)
        self.app.register_blueprint(collection.get_blueprint())