from api.routes import app
@app.get("/")
def root_route():
    return {"Welcome": 200}
