import asyncio
from pymongo import AsyncMongoClient


uri = "mongodb://localhost:27017/"
client = AsyncMongoClient(uri)

async def main():
    try:
        # start example code here

        # end example code here

        await client.admin.command("ping")
        print("Connected successfully")

        # other application code

        await client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

asyncio.run(main())