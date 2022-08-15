import pymongo
client = pymongo.MongoClient("mongodb+srv://root:MySqlAdmin123$@cluster0.s5f4god.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhanshu",
    "email":"sudhanshu@ineuron.ai",
    "surname":"kumar"
    }
db1 = client['monogotest']
coll = db1['test']
coll.insert_one(d)
