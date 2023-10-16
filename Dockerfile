FROM python:3.9.8

WORKDIR /app
USER root:root

COPY .requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./http_main.py /app/main.py

ENTRYPOINT [ "python", "app/main.py" ]