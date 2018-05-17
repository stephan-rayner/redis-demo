FROM python:3.6

ADD ./ /application/src

VOLUME /application/src

WORKDIR /application/src



RUN pip install -r requirements.txt

CMD python app.py