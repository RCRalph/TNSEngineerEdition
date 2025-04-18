import logging
import os
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from src.model import CityConfiguration

CONFIG_DIRECTORY_PATH = Path(__file__).parents[1] / "config" / "cities"


app = FastAPI()
logger = logging.getLogger(__name__)


@app.get("/cities")
def cities():
    city_configurations: list[CityConfiguration] = []

    for file in filter(lambda x: x.is_file(), CONFIG_DIRECTORY_PATH.iterdir()):
        try:
            city_configurations.append(
                CityConfiguration.model_validate_json(file.read_text())
            )
        except ValidationError as exc:
            logger.exception(f"Invalid configuration file: {file.name}", exc_info=exc)
            return JSONResponse("Invalid configuration files", 500)

    return city_configurations


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=os.environ.get("APP_HOST", "127.0.0.1"),
        port=os.environ.get("APP_PORT", 8000),
    )
