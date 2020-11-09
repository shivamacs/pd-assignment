import time
from aiohttp import web

result = {}

async def handle(request):
    text = request.match_info.get('param', "Home")
    
    if text == 'q1' and text not in result:
        for _ in range(12):
            print("processing")
            time.sleep(5)

        result[text] = f'Response for query: {text}'

    print('query processed')
    return web.Response(text=result[text])

app = web.Application()
app.add_routes([web.get('/', handle), web.get('/{param}', handle)])

if __name__ == '__main__':
    web.run_app(app)