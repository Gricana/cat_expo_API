FROM python:3.10

RUN apt-get update && apt-get install -y gcc libpq-dev postgresql-client  \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /expo

COPY requirements.txt .

RUN pip install --upgrade pip  \
    && pip install --no-cache-dir -r requirements.txt  \
    && pip install --no-cache-dir gunicorn

COPY . .

EXPOSE 8080
