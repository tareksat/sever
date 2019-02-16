import pymongo


class Database(object):

    URL = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URL)
        Database.DATABASE = client['controller']

    @staticmethod
    def load(collection):
        return [x for x in Database.DATABASE[collection].find({})]

    @staticmethod
    def find_by_id(collection, query):
        try:
            x = Database.DATABASE[collection].find(query)
            return x[0]
        except:
            pass

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=False)

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def delete(collection, query):
        Database.DATABASE[collection].remove(query)
