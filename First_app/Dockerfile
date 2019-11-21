FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
CMD python3 /app/main.py