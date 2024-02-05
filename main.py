from fastapi import FastAPI

app = FastAPI(
    title="Name - FastAPI",
    description="Name file Fast API ",
)

@app.get("/")
async def name():
    return {"name": "My name is Prasanthi."}


