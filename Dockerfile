# what os?
FROM python:3.9-slim

# add .dockerignore
COPY . /app
WORKDIR /app

# what to install for this os
RUN apt-get update --fix-missing && \
    apt-get -y install gcc mono-mcs && \
    apt-get install -y wget bzip2 ca-certificates curl git nano locales locales-all && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHON_VERSION=3.9
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV DEBIAN_FRONTEND=noninteractive


# what to install for this app
RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install -r requirements.txt


# what to run
CMD ["./run.sh"]