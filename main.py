import logging
from fastapi import FastAPI, Response
import time
import random
import string

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='./server.log')
formatter = logging.Formatter(
    "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
)

ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)  # Exporting logs to the screen
logger.addHandler(fh)  # Exporting logs to a file

logger = logging.getLogger(__name__)


@app.middleware("http")
async def log_requests(request, call_next):
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

    return response


@app.get("/people/{person_id}", status_code=200)
async def read_person(response: Response, person_id: int):
    if person_id > 100:
        response.status_code = 404
        return {"message": "person_id > 100"}
    return {"item_id": person_id}


@app.get("/planets/{planet_id}", status_code=200)
async def read_planet(response: Response, planet_id: int):
    if planet_id > 100:
        response.status_code = 404
        return {"message": "planet_id > 100"}
    return {"planet_id": planet_id}


@app.get("/starships/{starship_id}", status_code=200)
async def read_starship(response: Response, starship_id: int):
    if starship_id > 100:
        response.status_code = 404
        return {"message": "starship_id > 100"}
    return {"starship_id": starship_id}

# uvicorn main:app --reload
