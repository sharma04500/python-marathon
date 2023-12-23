import requests

response = requests.get("https://api.github.com/repos/devopsyuva/kubernetes_latest_manifest/commits").json()

for i in range(len(response)):
    print("id:", response[i]["sha"], "is committed by:", response[i]["commit"]["author"]["name"])

#   In general the api calls made to github will print the response code only. In order to fetch the entire data,
# json() function is used. The data is being fed to the variable `response`