from aiohttp import web
import json
from service import read_all_news_feeds

DATE_TIME_FORMAT='%Y/%m/%d %H:%M:%S'

async def index(request):
    response_obj = { 'status' : 'ok'}
    return web.Response(text=json.dumps(response_obj))

async def get_feeds(request):
    data = await request.json()
    terms = data.get('terms', [])
    limit = data.get('limit', None)
    feeds = list(read_all_news_feeds(terms))
    feeds.sort(key=lambda x: x.published_date, reverse=True)
    results = feeds[:limit] if limit else feeds
    return web.Response(
        status=200, 
        body=json.dumps([{'title': feed.title, 'link': feed.link, 'published_date': feed.published_date.strftime(DATE_TIME_FORMAT)} for feed in feeds], indent=4).encode('UTF-8'),
        content_type='application/json'
    )

async def refresh(request):
    data = await request.json()
    terms = data.get('terms', [])
    limit = data.get('limit', None)
    feeds = list(read_all_news_feeds(terms))
    feeds.sort(key=lambda x: x.published_date, reverse=True)
    results = feeds[:limit] if limit else feeds
    return web.Response(
        status=200, 
        body=json.dumps([{'title': feed.title, 'link': feed.link, 'published_date': feed.published_date.strftime(DATE_TIME_FORMAT)} for feed in feeds], indent=4).encode('UTF-8'),
        content_type='application/json'
    )

async def web_app():
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_post('/api/feeds', get_feeds)
    app.router.add_post('/refresh', refresh)
    return app

if __name__=='__main__':
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_post('/api/feeds', get_feeds)
    app.router.add_post('/refresh', refresh)
    web.run_app(app)