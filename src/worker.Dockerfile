FROM python:3.10-bullseye
RUN mkdir -p /app && mkdir -p /app/rabbitmq_service
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY worker/* .
COPY rabbitmq_service/* rabbitmq_service/
COPY worker/config.py .
CMD ["sh","-c","sleep 10 && python3 worker.py"]