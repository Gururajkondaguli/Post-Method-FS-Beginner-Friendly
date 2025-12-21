from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient




app = FastAPI()




# 🔥 CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["user_db"]
collection = db["users"]



# Schema
class UserName(BaseModel):
    name: str




#api
@app.post("/submit-name")
async def submit_name(user: UserName):
    result = await collection.insert_one({"name": user.name})
    return {
        "message": "Saved successfully",
        "id": str(result.inserted_id)
    }
