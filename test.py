import requests

print("Sending research request...\n")

response = requests.post(
    "http://127.0.0.1:8000/research",
    json={
        "topic": "Artificial Intelligence in Healthcare"
    },
    timeout=300
)

print("Status Code:", response.status_code)
print()
print(response.text)