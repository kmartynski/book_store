from fastapi import FastAPI

app = FastAPI()


@app.get("/books")
async def get_all_books():
    pass


@app.post("/books")
async def post_book():
    pass
