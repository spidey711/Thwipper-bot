import aiohttp
import aiofiles
import requests

from io import BytesIO
from bs4 import BeautifulSoup

async def get_async(url: str, headers: dict = {}, kind: str = "content"):
    """
    Simple Async get request
    """
    output = ""
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            if kind == "json":
                try:
                    output = await resp.json()
                except Exception as e:
                    print(e)
                    output = await resp.text()
            elif kind.startswith("file>"):
                f = await aiofiles.open(kind[5:], mode="wb")
                await f.write(await resp.read())
                await f.close()
                return
            elif kind == "fp":
                output = BytesIO(await resp.read())
            else:
                output = await resp.text()

        await session.close()
    return output

def fetch_dialogues():
    html = requests.get("https://geektrippers.com/spiderman-quotes/").content.decode()
    soup = BeautifulSoup(html, 'lxml')
    print(soup)