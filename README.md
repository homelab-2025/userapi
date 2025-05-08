## userapi

This is a small REST API used to do CRUD operation on MongoDB usersdb database.

## Summary

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Running the Application](#running-the-application)
* [API Documentation](#api-documentation)
* [Usage](#usage)
* [Testing](#testing)

## Prerequisites

- [Python 3.6+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
- [Make](https://gnuwin32.sourceforge.net/packages/make.htm)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Installation

1. Clone the repository:

```bash
git clone https://gitlab.com/homelab-2025/userapi.git
cd userapi
```

2. Then to create a virtual environment and to install packages, type in your terminal:

```bash
make install
```

[Back to top](#userapi)

## Running the Application

### On host

To run the application using a self hosted mongodb (usersdb need to be already created):

```bash
make run
```

### On Docker

To run the application using Docker Compose:

```bash
make cup
```

Then to shut it down:

```bash
make cdown
```

[Back to top](#userapi)

## API Documentation

Once the application is running, you can access the interactive API documentation at:

- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

[Back to top](#userapi)

## Usage

You can find sample httpie queries in the `sample_queries.md` file.

[Back to top](#userapi)

## Testing

To run the tests, you can use:

```bash
make tests
```

[Back to top](#userapi)