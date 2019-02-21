FROM docker.io/alpine
RUN apk update
RUN apk add libffi \
    libffi-dev \
    py-curl \
    openssl-dev
RUN apk add  \
    python \
    python-dev \
    py-pip \
    build-base \
  && rm -rf /var/cache/apk/*
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN mkdir /app
COPY GetPanel.py /app/
COPY monbot.py /app/
RUN chmod +x /app -R
ENTRYPOINT ["/usr/bin/python", "/app/MonBot.py"]
