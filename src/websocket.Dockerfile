FROM python:3.10-bullseye
RUN mkdir -p /app && mkdir -p /app/rabbitmq_service
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY websocket_api/* .
COPY rabbitmq_service/* rabbitmq_service/
COPY websocket_api/config.py .
CMD ["python3","websocket_api.py"]