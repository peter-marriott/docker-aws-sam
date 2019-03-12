FROM python:3.6.5-stretch

RUN mkdir /src
COPY ./requirements.txt /src/

RUN cd /src && pip install -r requirements.txt

COPY ./src/* /src/

EXPOSE 5000

CMD export FLASK_APP=/src/app1.py && export FLASK_ENV=development && flask run --host=0.0.0.0