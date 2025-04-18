import json
import pickle
import zipfile

import networkx as nx
import overpy
import pytest
from src.model.city_configuration import CityConfiguration
from src.model.gtfs_package import GTFSPackage


@pytest.fixture
def gtfs_package():
    return GTFSPackage.from_file("tests/assets/gtfs_schedule.zip")


@pytest.fixture
def relations_and_stops_overpass_query_result() -> overpy.Result:
    with zipfile.ZipFile(
        "tests/assets/relations_and_stops_overpass_query_result.zip"
    ) as zip_file:
        with zip_file.open("relations_and_stops_overpass_query_result.pickle") as file:
            return pickle.load(file)


@pytest.fixture
def krakow_tram_network_graph() -> nx.DiGraph:
    with zipfile.ZipFile("tests/assets/krakow_tram_network_graph.zip") as zip_file:
        with zip_file.open("krakow_tram_network_graph.pickle") as file:
            return pickle.load(file)


@pytest.fixture
def tram_trips_by_id() -> dict[str, list[int]]:
    with zipfile.ZipFile("tests/assets/tram_trips_by_id.zip") as zip_file:
        with zip_file.open("tram_trips_by_id.json") as file:
            return json.load(file)


@pytest.fixture
def krakow_city_configuration():
    with open("tests/assets/krakow_city_configuration.json") as file:
        return CityConfiguration.model_validate_json(file.read())
