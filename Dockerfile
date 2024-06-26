FROM python:3.8

WORKDIR /app

COPY . /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH /app

CMD ["pytest", "-s"]