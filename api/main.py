from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import uvicorn
from DB import fire as db
# import json

app = FastAPI()

class TrafficLight(BaseModel):
    latitude: float
    longitude: float
    name: str
    light: str

database = db
crossroads = db.getAllCrossroads()



# crossroads_1 = TrafficLight(latitude=40.7128, longitude=-74.0060, special_number="TL001", crossroad_name="Main Street")
# crossroads_2 = TrafficLight(latitude=34.0522, longitude=-118.2437, special_number="TL002", crossroad_name="Broadway Avenue")

# crossroads.update({crossroads_1.special_number: crossroads_1})
# crossroads.update({crossroads_2.special_number: crossroads_2})



@app.get("/crossroads/", response_model= dict)
async def get_crossroads():
    return crossroads

@app.get("/crossroads/{crossroad_name}", response_model=dict)
async def get_crossroad(crossroad_name: str):
    crossroad_data = database.getCrossroadByName(crossroad_name)
    
    if crossroad_data is not None:
        return crossroad_data
    else:
        raise HTTPException(status_code=404, detail=f"Crossroad '{crossroad_name}' not found")
    

@app.post("/crossroads/create")
async def add_crossroad(tl: TrafficLight):
    database.addOrUpdateCrossroad(tl)

    req_info = crossroads
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }


@app.post("/crossroads/update")
async def post_crossroad(tl: dict):
    database.addOrUpdateCrossroad(tl)

    req_info = crossroads.json()
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }

@app.put("/crossroads/{tl}")
async def change_light(tl: str):
        return database.changeCrossroadLight(tl)


@app.delete("/crossroads/{crossroads_name}")
async def delete_crossroad(crossroads_name: str):
    result = database.deleteCrossroad(crossroads_name)
    return {
        "status" : result,
    }

 
#uvicorn.run(app, host="0.0.0.0", port=8002)