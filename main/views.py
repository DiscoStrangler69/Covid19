from django.shortcuts import render
import requests
import json

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"Pakistan"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "21badd5a3dmsh709bb9301d6c1dep1c1e1cjsnf0778375794a"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data = response['response']
    d = data[0]
    context = {
        'all':d['cases']['total'],
        'recovered':d['cases']['recovered'],
        'deaths':d['deaths']['total'],
        'new':d['cases']['new'],
        'critical':d['cases']['critical']
    }
    print(d)
    return render(request, r"C:\Users\DELL\Desktop\Covid19\covid\\templates\index.html",context)
