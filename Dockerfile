FROM alpine:latest

RUN apk add nginx python3 bash && pip3 install --upgrade pip && pip3 install django gunicorn jinja2

COPY configurator /configurator
COPY entrypoint.sh /entrypoint.sh
RUN install -d -o nginx -g nginx -m 0770 /run && chmod +x /entrypoint.sh /configurator/*py

VOLUME [ "/logs", "/django" ]
WORKDIR [ "/django" ]
ENTRYPOINT [ "/entrypoint.sh" ]
