from ghibli_api.api_client import ApiClient
from ghibli_api.enums import ResponseCode


def test_all_films_from_api():
    """
    Check if Ghibli API provides not empty list of films, and with needed fields.
    """
    api_response = ApiClient.get_all_films_response()
    api_response_json = api_response.json()
    assert api_response.status_code == ResponseCode.OK
    assert isinstance(api_response_json, list)
    assert len(api_response_json) > 0
    assert isinstance(api_response_json[0]["people"], list)


def test_all_people_from_api():
    """
    Check if Ghibli API provides not empty list of people, and with needed fields.
    """
    api_response = ApiClient.get_all_people_response()
    api_response_json = api_response.json()
    assert api_response.status_code == ResponseCode.OK
    assert isinstance(api_response_json, list)
    assert len(api_response_json) > 0
    assert isinstance(api_response_json[0]["films"], list)
