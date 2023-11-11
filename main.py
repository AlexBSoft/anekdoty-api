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
def get_by_string(string: str, randomize: bool = False, limit: int = 10, offset: int = 0):
    results = []
    with open("./aneks.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        for i in range(len(data)):
            obj = data[i]
            if string in obj:
                results.append(obj)
    if(randomize):
        random.shuffle(results)
 
    return JSONResponse(content=results[:limit][offset:])

# Find in json exclusive by string
@app.get("/search_exclusive/{string}")
def get_by_string_exclusive(string: str, randomize: bool = False, limit: int = 10, offset: int = 0):
    results = []
    with open("./aneks.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        for i in range(len(data)):
            obj = data[i]
            if string not in obj:
                results.append(obj)
    if(randomize):
        random.shuffle(results)
    return JSONResponse(content=results[:limit][offset:])