import json
import random
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/random_anek")
def get_random_string():
    with open("./aneks.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        random_string = random.choice(data)
        return Response(content=random_string, media_type="text/plain")