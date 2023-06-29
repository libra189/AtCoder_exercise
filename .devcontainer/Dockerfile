ARG PYTHON_VERSION=3.11.2
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ENV PYTHONPATH=/app

RUN apt-get update && \
    apt-get install -y git

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    python -m pip install -r requirements.txt

COPY . .

CMD ["bash"]
