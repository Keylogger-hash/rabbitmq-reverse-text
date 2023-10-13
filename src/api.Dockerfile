FROM python:3.10-bullseye
RUN mkdir -p /app && mkdir -p /app/rabbitmq_service
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY http_api/* .
COPY rabbitmq_service/* rabbitmq_service/
COPY http_api/config.py .

CMD ["python3","main.py"]