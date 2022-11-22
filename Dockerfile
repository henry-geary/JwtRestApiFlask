FROM python:3.7-alpine

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir
EXPOSE 4000
COPY . .
ENTRYPOINT python app/__main__.py