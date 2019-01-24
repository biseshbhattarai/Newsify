import requests
from requests_jwt import JWTAuth

auth = JWTAuth('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ4MjU1MTU2LCJqdGkiOiJjYmRkYTQ1OWI2NTY0ZmY0OTNjN2EyYjJjN2JiMWM0NCIsInVzZXJfaWQiOjF9.fTtrAwhhglWmLwlFgGWj_Pu-U0rGulpReaz3mfFKIcw')
res = requests.get("http://127.0.0.1:8000/news", auth=auth)
print(res.json())