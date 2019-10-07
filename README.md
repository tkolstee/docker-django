# docker-django

A Docker container based upon nginx and gunicorn, which is designed to serve up a single preexisting django project

## Usage:

Simple scenario:

```$ django-admin startproject myproject```
Edit myproject/myproject/settings.py, adding server hostname(s) to ALLOWED_HOSTS
```
$ docker run \
  -e PROJECT_NAME=myproject \
  -e SERVER_NAMES=myhostname.domain.com,myhostname \
  -p 8888:80 \
  -v $(pwd)/logs:/logs \
  -v $(pwd)/myprject:/django \
  tkolstee/docker-django:latest
```
The test site is now accessible as http://myhostname.domain.com:8888/



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

