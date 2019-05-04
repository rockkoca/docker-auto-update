FROM python:3.7.3

RUN curl -fsSL get.docker.com -o get-docker.sh;sh get-docker.sh; rm get-docker.sh;
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./app.py /app.py

ENTRYPOINT ["python", "/app.py"]