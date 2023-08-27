FROM python:3.9

RUN pip install fastapi uvicorn[standrad] paho-mqtt


COPY ./main.py /main.py


#RUN uvicorn main:app --reload --host 0.0.0.0

EXPOSE 8001

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8001