from ghibli_api.models import PeopleToMovieMap


class ApiInfoExtractor:
    @staticmethod
    def get_people_to_movie_maps(all_films, all_people):
        maps_collection = []
        for film in all_films:
            map_ = PeopleToMovieMap(movie_title=film["title"])
            maps_collection.append(map_)
            for person in all_people:
                if film["id"] in ",".join(person["films"]):
                    map_.people.append(person["name"])
        return maps_collection
