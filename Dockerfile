FROM python:3 as package
WORKDIR /web
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel -w /root/wheels --no-cache-dir -r requirements.txt

FROM python:3 as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG PORT
WORKDIR /web

RUN apt-get update -y \
  && apt-get -f install \
  && apt-get upgrade -y \
  && pip install --upgrade pip

COPY --from=package /root/wheels /root/wheels
COPY requirements.txt .
RUN pip install --no-index --find-links=/root/wheels -r requirements.txt

EXPOSE ${PORT}
