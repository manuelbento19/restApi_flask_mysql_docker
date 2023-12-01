FROM python:3.6

WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install -r requirements.txt

ENV FLASK_APP=./src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

COPY . /backend/

CMD ["flask", "run","--host","0.0.0.0"]