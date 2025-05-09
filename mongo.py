from pymongo import MongoClient
#pip install pymongo
client=MongoClient("mongodb://local host:27017/")
db=client["mydatabase"]
collection=db["users"]

print("===CREATE===")
user1={"name":"Master","age":30,"email":"master@gmail.com"}
user2={"name":"faster","age":35,"email":"bobs@gmail.com"}
user3={"name":"waste","age":35,"email":"waste@gmail.com"}
print(collection.insert_one(user1))
print(collection.insert_many([user2,user3]))
print("\n===READ===")
alice=collection.find_one({"name":"Master"})
print("Find one:",alice)
print("Find all:")
for user in collection.find():
    print(user)

print("\n===UPDATE===")
collection.update_one({"name":"Master"},{"$set":{"age":31}})
updated_alice=collection.find_one({"name":"Master"})
print("updated Alice:",updated_alice)

collection.update_many({"age":{"$lt":30}},{"$set":{"status":"young"}})
print("After bulk update:")
for user in collection.find():
    print(user)

print("\n===DELETE===")
collection.delete_one({"name":"faster"})
print("After deleting Bob:")
for user in collection.find():
    print(user)

collection.delete_many({"age":{"$gte":30}})
print("After deleting users aged 30+:")
for users in collection.find():
    print(user)


client.close()
