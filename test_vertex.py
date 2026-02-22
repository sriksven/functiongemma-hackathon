import urllib.request, json, urllib.parse

def _get_access_token():
    url = "https://oauth2.googleapis.com/token"
    data = urllib.parse.urlencode({
        "client_id": "764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com",
        "client_secret": "YOUR_CLIENT_SECRET",
        "refresh_token": "YOUR_REFRESH_TOKEN",
        "grant_type": "refresh_token"
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())["access_token"]

token = _get_access_token()
print("Token retrieved.")

models = [
    "gemini-2.0-pro-exp-02-05", 
    "gemini-1.5-pro-002",
    "gemini-2.5-pro"
]

for m in models:
    url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/artful-sled-488116-a4/locations/us-central1/publishers/google/models/{m}:generateContent"
    payload = {"contents": [{"role": "user", "parts": [{"text": "hi"}]}]}
    req = urllib.request.Request(
            url, 
            data=json.dumps(payload).encode("utf-8"),
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Model {m} SUCCESS")
    except Exception as e:
        print(f"Model {m} FAILED: {e}")
