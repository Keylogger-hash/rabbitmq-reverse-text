import os

worker_queue = "reverse_text_queue"
worker_queue_results = "worker_results_queue"
rabbitmq_url = os.environ.get("RABBITMQ_URL")
