import pymongo

client = pymongo.MongoClient("mongodb+srv://root:MySqlAdmin123$@cluster0.s5f4god.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["sudh"]

'''
record = collection.find()
for i in record:
    print(i)
'''

data = collection.find({"companyName": "iNeuron"})
data2 = collection.find({'courseOffered':{"$gt":"E"}})
for i in data2:
    print(i)