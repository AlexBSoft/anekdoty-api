import json
import random
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/random_anek")
def get_random_string():
    with open("./aneks.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        random_string = random.choice(data)
        return Response(content=random_string, media_type="text/plain")
    
# Find in json by string
@app.get("/search/{string}")
def get_by_string(string):
    results = []
    with open("./aneks.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        for obj in data:
            if string in obj["text"]:
                results.append(obj["text"])
    return JSONResponse(content=results)

# Find in json exclusive by string
@app.get("/search_exclusive/{string}")
def get_by_string_exclusive(string):
    results = []
    with open("./aneks.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        for obj in data:
            if string in obj["text"] and obj["text"] not in results:
                results.append(obj["text"])
    return JSONResponse(content=results)