FROM python:3-alpine

WORKDIR /backend

COPY requirements.txt /backend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=./src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

COPY . .

CMD ["flask", "run"]