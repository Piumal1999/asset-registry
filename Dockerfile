FROM python:3.10.1-slim

ARG PORT=5000

WORKDIR /app
COPY . /app

#RUN apt-get update && apt-get upgrade -y
RUN pip3 install -r requirements.txt

RUN groupadd -g 61000 assetuser && useradd -g 61000 -l -M -s /bin/false -u 61000 assetuser
USER assetuser

EXPOSE $PORT
ENTRYPOINT ["gunicorn"]
CMD ["asset_app:app","-b",":5000","--workers","4","--log-level","debug","--worker-class","gevent","--preload"]

HEALTHCHECK --interval=5m --timeout=3s CMD wget --no-verbose  --spider http://localhost:5000/health || exit 1
