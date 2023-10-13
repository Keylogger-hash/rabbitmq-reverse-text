# Rabbitmq reverse text service

## Setup
Run docker-compose
1. ```cd src/```
2. ```cp .env env.example```
3. ```docker-compose up --build -d```

## Testing
Instruction testing service
1. ```cd src/```
2. ```virtualenv venv```
3. ```source venv/bin/activate```
4. ```python3 queue_reverse_text.py```
5. ```python3 listen_result.py```

Input your message in queue_reverse_text.py.<br/>
Get your reverse message in listen_result.py

