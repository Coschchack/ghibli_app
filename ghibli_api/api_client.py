import requests
from concurrent import futures


class ApiClient:
    @staticmethod
    def get(endpoint):
        return requests.get(endpoint)

    def get_concurrently(self, endpoints):
        with futures.ThreadPoolExecutor(max_workers=len(endpoints)) as executor:
            results = executor.map(self.get, endpoints)
        return [result.json() for result in results]
