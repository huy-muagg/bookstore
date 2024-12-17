# BookStore

BookStore description

## Quick Start

Install the dependencies and run the application:

    poetry install
    poetry run flask --debug run

And open it in the browser at [http://localhost:5000/](http://localhost:5000/)

## Prerequisites

Python >=3.8

## Development environment

This project uses [Poetry](https://python-poetry.org/docs/).

Quick start:

    poetry install

    poetry run pytest
    poetry run black [--check] .
    poetry run isort [--check] .

Run a development server in debug mode (changes in are reloaded automatically):

    poetry run flask --app bookstore --debug run

## Configuration

Default configuration is loaded from `bookstore.defaults` and can be
overriden by environment variables with a `FLASK_` prefix. See
[Configuring from Environment Variables](https://flask.palletsprojects.com/en/3.0.x/config/#configuring-from-environment-variables).

Consider using
[dotenv](https://flask.palletsprojects.com/en/3.0.x/cli/#environment-variables-from-dotenv).

## Deployment

See [Deploying to Production](https://flask.palletsprojects.com/en/3.0.x/deploying/).

You may use the distribution (`make dist`) to publish it to a package index,
deliver to your server, or copy in your `Dockerfile`, and insall it with `pip`.

You must set a
[SECRET_KEY](https://flask.palletsprojects.com/en/3.0.x/tutorial/deploy/#configure-the-secret-key)
in production to a secret and stable value.
