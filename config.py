import os
from urlparse import urlparse
from dotenv import load_dotenv

# Load '.env' if it exists.
load_dotenv()

#
# We configure Sixpack using environment variables, rather than
# the default `config.yml`. This allows us to easily change settings
# with the Heroku control panel rather than storing them in Git!
#
# For available environment variables: https://git.io/fNF62
#

# We protect the admin interface with HTTP Basic Auth:
username = os.environ['ADMIN_USERNAME']
password = os.environ['ADMIN_PASSWORD']

# If using Heroku's Redis addon, parse 'REDIS_URL':
if 'REDIS_URL' in os.environ:
    redis_endpoint = urlparse(os.environ.get('REDIS_URL'))

    os.environ['SIXPACK_CONFIG_REDIS_HOST'] = redis_endpoint.hostname
    os.environ['SIXPACK_CONFIG_REDIS_PORT'] = str(redis_endpoint.port)
    os.environ['SIXPACK_CONFIG_REDIS_PASSWORD'] = redis_endpoint.password
    os.environ['SIXPACK_CONFIG_REDIS_DB'] = '0'
