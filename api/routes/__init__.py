from fastapi import FastAPI
app = FastAPI()
# Root Route
from api.routes.home import root_route
# Data Route
from api.routes.data import get_data_route
from api.routes.data import post_data_route
from api.routes.data import put_data_route
from api.routes.data import delete_data_route
