import pytest

from ghibli_api.api_info_extractor import ApiInfoExtractor


ALL_FILMS_API_RESP_MOCK = [
    {
        "id": "id1",
        "title": "movie1",
    },
    {
        "id": "id2",
        "title": "movie2",
    },
]

ALL_PEOPLE_API_RESP_MOCK = [
    {
        "name": "name1",
        "films": [
            "id1",
            "id2",
        ]
    },
    {
        "name": "name2",
        "films": [
            "id1",
            "id2",
        ]
    },
]


@pytest.fixture(scope="module")
def maps_collection():
    return ApiInfoExtractor().get_people_to_movie_maps(
        all_films=ALL_FILMS_API_RESP_MOCK, all_people=ALL_PEOPLE_API_RESP_MOCK)


def test_map_format(maps_collection):
    """
    Check if the format of the returned maps collection is as expected by the application.
    """
    assert isinstance(maps_collection, (list, tuple))
    assert len(maps_collection) > 0
    sample_map = maps_collection[0]
    assert isinstance(sample_map.movie_title, str)
    assert isinstance(sample_map.people, list)


def test_extracted_films(maps_collection):
    """
    Check if the extracting code properly extracts info about the films.
    """
    mock_films = sorted([mock_film["title"] for mock_film in ALL_FILMS_API_RESP_MOCK])
    map_films = sorted([map_.movie_title for map_ in maps_collection])
    assert map_films == mock_films


def test_extracted_people(maps_collection):
    """
    Check if the extracting code properly extracts info about the people.
    """
    people_from_mapper = []
    for map_ in maps_collection:
        people_from_mapper.extend(map_.people)
    unique_people_from_mapper = sorted(set(people_from_mapper))
    mock_people = sorted((person["name"] for person in ALL_PEOPLE_API_RESP_MOCK))
    assert unique_people_from_mapper == mock_people
