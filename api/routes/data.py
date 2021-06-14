from api.routes import app
from typing import Optional

@app.get("/data/get/{data_id}")
def get_data_route(data_id: int, query: Optional[str] = None):
    return {
        "status": 200,
        "data_id": data_id,
        "query": query,
        "data": {}
    }

@app.put("/data/put/{data_id}")
def put_data_route(data_id: int): ...

@app.post("/data/post/")
def post_data_route(data_id: int): ...

@app.delete(("/data/delete/{data_id}"))
def delete_data_route(data_id: int): ...
