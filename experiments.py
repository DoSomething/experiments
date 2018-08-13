#
# This is a simple wrapper application for Seatgeek's
# Sixpack A/B testing framework! We use it to host both the
# web and API processes on the same Heroku dyno.
#

import config

from routes import Mapper
from sixpack.web import start as sixpack_web
from sixpack.server import start as sixpack_api
from werkzeug.wrappers import Request, Response

class Application(object):
    def __init__(self):
        self.map = Mapper()

        # Map '/api' to the Sixpack API server.
        self.map.connect('api', '/api', path_info='/', app=sixpack_api)
        self.map.connect('api', '/api/{path_info:.*}', app=sixpack_api)

        # Map anything else to the Sixpack web interface.
        self.map.connect('web', '{any:.*?}', app=sixpack_web)

    def authorized(self, environ):
        request = Request(environ)
        auth = request.authorization
        return auth and auth.username == config.username and \
            auth.password == config.password

    def require_auth(self, environ, start_response):
        response = Response('You need to log in to access that.', 401,
                        {'WWW-Authenticate': 'Basic realm=sixpack'})
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        match, route = self.map.routematch(environ=environ)

        # If app is not being served from the root, set expected
        # PATH_INFO (e.g. '/api/participate' to '/participate')
        if 'path_info' in match:
            environ['PATH_INFO'] = match['path_info']

        # If we're on the web interface, protect w/ basic auth.
        if route.name == 'web' and not self.authorized(environ):
            return self.require_auth(environ, start_response)

        return match['app'](environ, start_response)

app = Application()
