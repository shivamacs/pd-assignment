import asyncio
import os
from aiohttp import ClientSession

async def send_request(session, url):
    print('request pending')
    res = await session.get(url)
    print(await res.text())

async def main():
    async with ClientSession() as session:
        tasks = []
        for _ in range(10):
            tasks.append(send_request(session, 'http://localhost:8080/q1'))

        combined = await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())