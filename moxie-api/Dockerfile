FROM python:3.10

WORKDIR /usr/src/app


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000