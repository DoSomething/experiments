# DoSomething.org Experiments

This is the DoSomething.org experiments service, powered by [Sixpack](http://sixpack.seatgeek.com).

## Contributing

Install [Python](https://www.python.org) and [VirtualEnv](https://virtualenv.pypa.io/en/stable/). You'll also need a local [Redis](https://redis.io) database.

```sh
# Create virtual environment:
virtualenv venv
source venv/bin/activate

# Install dependencies:
$ pip install -r requirements.txt

# Copy environment variables & edit w/ your machine's details:
$ cp .env.example .env && vi .env

# And finally, start your local dev server!
$ gunicorn experiments:app
```

## Security Vulnerabilities

We take security very seriously. Any vulnerabilities in Experiments should be reported to [security@dosomething.org](mailto:security@dosomething.org),
and will be promptly addressed. Thank you for taking the time to responsibly disclose any issues you find.

## License

&copy; DoSomething.org. Experiments is free software, and may be redistributed under the terms specified
in the [LICENSE](https://github.com/DoSomething/bertly/blob/master/LICENSE) file. The name and logo for
DoSomething.org are trademarks of Do Something, Inc and may not be used without permission.
