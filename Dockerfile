FROM python:3.9 as package
WORKDIR /web
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel -w /root/wheels --no-cache-dir -r requirements.txt

FROM python:3.9 as builder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG PORT
WORKDIR /web

RUN apt-get update -y \
  && apt-get -f install \
  && apt-get upgrade -y \
  && apt-get -y install curl gcc build-essential\
  && apt-get -y install libpq-dev --no-install-recommends apt-utils \
  && pip install --upgrade pip

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get -qq install nodejs --yes

COPY --from=package /root/wheels /root/wheels
COPY requirements.txt .
RUN pip install --no-index --find-links=/root/wheels -r requirements.txt

EXPOSE ${PORT}
