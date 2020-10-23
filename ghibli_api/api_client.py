import asyncio

import requests
from aiohttp import ClientSession


class ApiClient:
    @staticmethod
    def get(endpoint):
        return requests.get(endpoint)

    @staticmethod
    async def async_get(client_session, url_, **kwargs):
        async with client_session.get(url_, verify_ssl=False, **kwargs) as resp:
            resp_json = await resp.json()
            return resp_json

    async def async_gets(self, urls):
        async with ClientSession() as session:
            coroutines = (self.async_get(session, url_) for url_ in urls)
            results = await asyncio.gather(*coroutines)
        return results
