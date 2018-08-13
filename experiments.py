#
# This is a simple wrapper application for Seatgeek's
# Sixpack A/B testing framework! We use it to host both the
# web and API processes on the same Heroku dyno.
#

import config

from routes import Mapper
from sixpack.server import start as sixpack_api
from sixpack.web import start as sixpack_web

class Application(object):
    def __init__(self):
        self.map = Mapper()

        # Map '/api' to the Sixpack API server.
        self.map.connect('api', '/api', path_info='/', app=sixpack_api)
        self.map.connect('api', '/api/{path_info:.*}', app=sixpack_api)

        # Map anything else to the Sixpack web interface.
        self.map.connect('web', '{any:.*?}', app=sixpack_web)

    def __call__(self, environ, start_response):
        match = self.map.routematch(environ=environ)

        if 'path_info' in match[0]:
            environ['PATH_INFO'] = match[0]['path_info']

        return match[0]['app'](environ, start_response)

app = Application()
