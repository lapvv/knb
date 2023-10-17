from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
app = FastAPI()
client = MongoClient("localhost", 27017)
db = client.gameDB
usersInDB = db.users
results = db.resultsDB
origins = ['http://127.0.0.1:8002', 'http://localhost:8080', 'http://192.168.1.7:8080']
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

user_counter = 1
usersLobby = []
round_id = 1

# @app.get("/", tags = ['LOGIN'])
# async def root() -> dict:
#     return {"Ping":"Pong"}

# @app.post("/", tags = ['LOGIN'])
# async def login(name) -> dict:
#     return {'data': name}

@app.get("/user", tags = ['users'])
async def get_user() -> dict:
    return usersInDB.find()

@app.post("/", tags = ['users'])
async def post_user(user: dict) -> dict:
    new_user = user
    global user_counter
    global usersLobby
    new_user['id'] = user_counter
    user_counter += 1
    # print("user name: ", user['name'])
    usersLobby.append(new_user)
    # print(usersInDB.find_one({"name": user['name']}))
    if not usersInDB.find_one({"name": user}):
        usersInDB.insert_one(new_user)
    for user in usersLobby:
        print(user)
    # print('length: ', len(usersLobby))
    if len(usersLobby) == 2:
        result = results.insert_one({"datetimestamp": datetime.now()})
        print(result)
        usersLobby = []
        # print(result._id)
        return { "data": "ready to play" }
    else:
        return { "data": 'added to queue'}
        # return {"data": 'added to queue: ' + str(new_user)}

@app.post("/game", tags = ['game'])
async def game_choice(user: dict, choice: str) -> dict:
    results.insert_one({"user": choice})
    return 


# @app.put("/user/{id}", tags = ['users'])
# async def update_user(id: int, body: dict) -> dict:
#     for user in users:
#         if int(user['id']) == id:
#             user['activity'] = body['activity']
#             return {"data": f'user with id = {id} has been updated successfully'}
#     return {"data": f"user with id = {id} wasn't found"}

# @app.delete("/user/{id}", tags = ['users'])
# async def delete_user(id: int) -> dict:
#     for user in usersInDB.find():
#         if int(user['id']) == id:
#             usersInDB.find_one_and_delete()
#             # usersInDB.delete_one(user)
#             return {"data": f'user with id = {id} has been deleted'}
#     return {"data": f"user with id = {id} wasn't found"}