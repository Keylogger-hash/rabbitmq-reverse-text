import requests

while True:
    message = input(str())
    r = requests.post("http://localhost:8000/queue_reverse_text", params={"text": message}, headers={"Content-Type": "application/json"},)
    if r.status_code == 200:
        print(f"Message sent successful: {message}")
    else:
        print("Message send failed")