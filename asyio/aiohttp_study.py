import asyncio

from aiohttp import web
# 显示为下载的原因是编码问题
#web.Response(body=b'<h1>Index</h1>', content_type='text/html', charset='UTF-8')
# 在这个里面加上content_type 与charset即可
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html', charset='UTF-8')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello,%s</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html', charset='UTF-8')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    print('Server started at http://127.0.0.1:8000')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
