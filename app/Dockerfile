# pull official base image
FROM python:3.8-slim-buster

# set work directory
ENV HOME=/usr/src/app
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y postgresql python3-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt $HOME
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh $HOME
RUN chmod 755 entrypoint.sh

# copy project
COPY . $HOME

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]