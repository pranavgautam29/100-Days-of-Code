import requests
from datetime import datetime

USERNAME = "pranavgautam"
TOKEN = "j204g485g08f9o3uf1h320"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes"

}
response1 = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

response2 = requests.post(
    url=graph_endpoint, json=graph_config, headers=headers)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2022, month=10, day=22)


pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "11.5"
}

response3 = requests.post(url=pixel_creation_endpoint,
                          json=pixel_params, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_data = {
    "quantity": "9"
}
response4 = requests.put(url=update_endpoint, json=new_data, headers=headers)
