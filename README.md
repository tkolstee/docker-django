# docker-django

A Docker container based upon nginx and gunicorn, which is designed to serve up a single preexisting django project

## Usage:

Simple scenario:

- In an empty directory, clone this repository and rename the checkout's directory to "build"
- Place your django project in the same directory as "build" - in this example "myproj"
- Create docker-compose.yml with the following content:

```
---
version: '3'
services:
  dj:
    build:
      context: build
    container_name: dj
    hostname: dj
    ports:
    - 8000:80
    volumes:
    - ./logs:/logs
    - ./myproj:/django
    environment:
    - PROJECT_NAME=myproj
```

- Run docker-compose build && docker-compose up -d
- Django project is now accessible from port 8000 on the host

## Variables:

The following environment variables affect the behavior of the installation:

|  Variable            |  Default Value  |  Description                                  |
|----------------------|-----------------|-----------------------------------------------|
| WORKER_PROCESSES     | 1024            | Number of worker processes for nginx          |
| NGINX_USER           | nginx           | Default user for nginx and gunicorn           |
| NGINX_GROUP          | nginx           | Default group for nginx and gunicorn          |
| WORKER_CONNECTION    | 5               | Number of worker connections                  |
| FAIL_TIMEOUT         | 0               | Timeout to fail socket conn (0=retry forever) |
| CLIENT_MAX_BODY_SIZE | 4G              | Max body size to accept from web client       |
| KEEPALIVE_TIMEOUT    | 5               | Keepalive timeout for nginx                   |
| STATIC_FILES_PATH    | current/public  | Path for static files relative to project dir |
| PROXY_BUFFERING      | True            | Set to false if using streaming connections   |
| PROJECT_NAME         | projname        | Django project name                           |
| SERVER_NAMES         | (my hostname)   | Delimited list of valid hostnames used        |


## Caveats

I'm new to Django and mostly pulled the Nginx/GUnicorn configs from tutorials.
This works as far as displaying the test page from a brand-new project with the default sqlite db.

