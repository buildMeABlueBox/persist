from pymongo import MongoClient
import requests

client = MongoClient() 
URL = "http://api.cbssports.com/fantasy/players/list"
PARAMS = {"version":"3.0", "SPORT":"football", "response_format":"JSON"}

r = requests.get(url=URL, params= PARAMS)

data = r.json()

print(data)

