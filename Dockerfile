FROM python:3.9-slim-buster
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /config
COPY ./src/main.py .
COPY ./src/config/param.yml ./config

CMD ["python3","main.py"]

