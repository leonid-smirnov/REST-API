FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_djangoAPI
WORKDIR /web_djangoAPI
COPY requirements.txt /web_djangoAPI/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_djangoAPI/