import requests

print("=" * 60)
print("      CogniResearch AI Chat")
print("Type 'exit' to quit")
print("=" * 60)

while True:
    topic = input("\nYou: ")

    if topic.lower() == "exit":
        break

    print("\nResearching...\n")

    try:
        response = requests.post(
            "http://127.0.0.1:8000/research",
            json={"topic": topic},
            timeout=600
        )

        if response.status_code == 200:
            data = response.json()

            print("=" * 80)
            print(data["report"])
            print("=" * 80)

        else:
            print(response.text)

    except Exception as e:
        print(e)