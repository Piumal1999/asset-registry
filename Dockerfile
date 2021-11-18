FROM python:3.8

ARG PORT=5000

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

RUN addgroup -S assetuser && adduser -S -G assetuser assetuser
USER assetuser

EXPOSE $PORT
ENTRYPOINT ["gunicorn"]
CMD ["app:app","-b",":5000"]

HEALTHCHECK --interval=5m --timeout=3s CMD wget --no-verbose  --spider http://localhost:5000/api/health || exit 1