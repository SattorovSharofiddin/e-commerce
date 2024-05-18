FROM python:3.10.2-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt && \
    apt-get update -y && \
    apt-get install -y netcat
#RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /app/requirements.txt && pip install gunicorn

COPY ./entrypoint.sh .
RUN chmod +x /code/entrypoint.sh

COPY . .

ENTRYPOINT ["/code/entrypoint.sh"]
