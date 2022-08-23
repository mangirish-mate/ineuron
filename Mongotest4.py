import pymongo

client = pymongo.MongoClient("mongodb+srv://root:MySqlAdmin123$@cluster0.s5f4god.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["sudh"]
