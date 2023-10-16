from fastapi import FastAPI
from pymongo import MongoClient
app = FastAPI()
client = MongoClient("localhost", 27017)
db = client.gameDB
usersInDB = db.users
results = db.resultsDB

# @app.get("/", tags = ['LOGIN'])
# async def root() -> dict:
#     return {"Ping":"Pong"}


user_counter = 1
# join_key = secrets.token_urlsafe(12)

@app.get("/user", tags = ['users'])
async def get_user() -> dict:
    return usersInDB.find()

@app.post("/user", tags = ['users'])
async def post_user(user: dict) -> dict:
    new_user = user
    global user_counter
    new_user['id'] = user_counter
    user_counter += 1
    # users.append(user)
    # print("user: ", user)
    # print("users: ", users)
    # print("user_counter: ", user_counter)
    usersInDB.insert_one(new_user)
    for user in usersInDB.find():
        print(user)
    return {"data": 'added: ' + str(new_user)}

# @app.put("/user/{id}", tags = ['users'])
# async def update_user(id: int, body: dict) -> dict:
#     for user in users:
#         if int(user['id']) == id:
#             user['activity'] = body['activity']
#             return {"data": f'user with id = {id} has been updated successfully'}
#     return {"data": f"user with id = {id} wasn't found"}

@app.delete("/user/{id}", tags = ['users'])
async def delete_user(id: int) -> dict:
    for user in usersInDB.find():
        if int(user['id']) == id:
            usersInDB.find_one_and_delete()
            # usersInDB.delete_one(user)
            return {"data": f'user with id = {id} has been deleted'}
    return {"data": f"user with id = {id} wasn't found"}