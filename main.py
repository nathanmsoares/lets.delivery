from typing import List
from fastapi import FastAPI, Request
from models import BaseM, Cat
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import logging
import uvicorn
# from support import db


log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["access"]["use_colors"] = True

app = FastAPI(log_config=log_config)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


# @app.on_event("startup")
# async def startup():
#     await db.database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await db.database.disconnect()


@app.get("/", response_model=List[BaseM])
async def read_notes():
    return "nothing"
    # query = db.notes.select()
    # return await db.database.fetch_all(query)


# @app.post("/")
# async def create_note(cat: BaseM):
#     print(cat)
    # query = db.notes.insert().values(text=note.text, completed=note.completed)
    # last_record_id = await db.database.execute(query)
    # return {**note.dict(), "id": last_record_id}
    #############################################################################################################

@app.put("/items/{item_id}")
async def update_item(item_id: int, baseM: BaseM, request: Request):
    json_compatible_item_data = jsonable_encoder(baseM)
    # logger.debug("teste")
    print(type(json_compatible_item_data))
    # print(log(request, json_compatible_item_data))
    # print(help(request))
    # print("user", request.user)
    print("url", request.url)
    print("state", request.state)
    # print("session", request.session)
    print("query_params", request.query_params)
    print("path_params", request.path_params)
    print("headers", request.headers)
    print("cookies", request.cookies)
    print("client", request.client)
    print("base_url", request.base_url)
    print(baseM.dict())
    # print("auth", request.auth)
    # print("app", request.app)
    # print("get", request.get)
    # print("items", request.items)
    # print("keys", request.keys)
    # print("values", request.values)
    # # def log(request: Request, content):
    #     #     logger.debug(f"[handler] {request.client} {content}")
