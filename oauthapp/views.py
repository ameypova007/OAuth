from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
import requests
import json
import os

redirect_uri = os.environ.get("REDIRECTURI")


def auth(request):
    if request.method == "GET":
        # print("dict", request.__dict__)
        print(request.GET.get("USER"))
        endpoint = "https://app-eu1.hubspot.com/oauth/authorize" \
                   "?client_id=57bee6b6-333d-4d78-bf0f-d53dcb4224f3" \
                   f"&redirect_uri={redirect_uri}" \
                   "&scope=contacts%20settings.users.write%20settings.users.read"
        print(endpoint)
        return redirect(endpoint)


def test(request):
    if request.method == "GET":
        code = request.GET.get("code")
        token_data = {
            "code": request.GET.get("code"),
            "client_id": "57bee6b6-333d-4d78-bf0f-d53dcb4224f3",
            "client_secret":"b5e88ba7-5739-47cb-bfff-b69369ceb04a",
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post("https://api.hubapi.com/oauth/v1/token", data=token_data, headers=headers)
        json_obj = json.loads(r.text)
        print(json_obj)
        url = "https://api.hubapi.com/oauth/v1/access-tokens/"+json_obj["access_token"]
        r = requests.get(url=url)
        print("user_info",r.text)
        # return JsonResponse({"code": json.loads(r.text)})
        return redirect(f"https://app-eu1.hubspot.com/integrations-settings/{json.loads(r.text)['hub_id']}/installed")
