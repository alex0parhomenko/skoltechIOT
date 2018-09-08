from aiohttp import web
import logging

logger = logging.getLogger(__name__)

async def ping(request):
    return web.json_response({'result': 'ok'}, status=200)
