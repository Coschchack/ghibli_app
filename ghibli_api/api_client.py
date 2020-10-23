import asyncio

import requests
from aiohttp import ClientSession


class ApiClient:
    SEMAPHORE = asyncio.BoundedSemaphore(10)

    @staticmethod
    def get(endpoint):
        return requests.get(endpoint)

    async def async_get(self, client_session, url_, **kwargs):
        # Also limit the number of concurrent requests
        async with self.SEMAPHORE, client_session.get(url_, verify_ssl=False, **kwargs) as resp:
            resp_json = await resp.json()
            return resp_json

    async def async_gets(self, urls):
        async with ClientSession() as session:
            coroutines = (self.async_get(session, url_) for url_ in urls)
            results = await asyncio.gather(*coroutines)
        return results
