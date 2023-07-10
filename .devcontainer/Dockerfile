ARG PYTHON_VERSION=3.11.2
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ENV PYTHONPATH=/app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade setuptools

ARG REQUIREMENTS=requirements.txt
COPY ${REQUIREMENTS} .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash"]
