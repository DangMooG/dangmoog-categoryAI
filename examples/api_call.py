import requests
import json



url = "http://127.0.0.1:8000/classification"

data = {"text":"CGV 2시 영화 티켓 팔아요"}

response = requests.post(url, json=data)

# 응답 텍스트를 JSON 형식으로 변환합니다.
response_text = json.loads(response.text)

print("status code: {}".format(response.status_code))
print("response: {}".format(response_text))