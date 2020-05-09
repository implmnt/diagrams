FROM python:3-alpine
WORKDIR /diagrams
RUN apk add --update --no-cache graphviz ttf-freefont && pip install diagrams
ENTRYPOINT /bin/sh
