FROM python:3.11.3-bullseye

WORKDIR /app

COPY ./ .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python3 manage.py runserver 0.0.0.0:3000
