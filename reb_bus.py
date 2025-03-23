import requests

url = "https://bus-route.p.rapidapi.com/getroute"

querystring = {"departure_place":"Delhi","arrival_place":"Gurugram"}

headers = {
	"x-rapidapi-key": "627aaf6ff3msh9a97d68095ba5ffp124465jsncdb1974baec8",
	"x-rapidapi-host": "bus-route.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())