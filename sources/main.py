from aiohttp import web
from routers import ping
import logging
import argparse

logging.basicConfig(filename='application.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='oh blya')
parser.add_argument('--port', '-p', type=str, help='webserver port')

args = parser.parse_args()

params = dict()


def main():
    app = web.Application()
    app.add_routes([web.get('/ping', ping)])
    web.run_app(app, port=args.port)


if __name__ == '__main__':
    main()
