import requests
import json


def initialization():
    url = 'https://kauth.kakao.com/oauth/token'
    rest_api_key = '9503d3d5f237eb8ef18d36edf9097747'
    redirect_uri = 'https://naver.com'
    authorize_code = 'KD04xFg6l7VTknzC7uG-iuQYXRdDoYb8RtJpR_1Cbmo-l9imdif5mHALdHcVteIKWLwXJwopb1UAAAGCOkwdPQ'

    data = {
        'grant_type':'authorization_code',
        'client_id':rest_api_key,
        'redirect_uri':redirect_uri,
        'code': authorize_code,
        }

    response = requests.post(url, data=data)
    tokens = response.json()
    print(tokens)


    with open("kakao_code.json","w") as fp:
        json.dump(tokens, fp)

def send(content):
    try:
        with open("kakao_code.json","r") as fp:
            tokens = json.load(fp)
    except:
        initialization()
        with open("kakao_code.json","r") as fp:
            tokens = json.load(fp)
    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers={
        "Authorization" : "Bearer " + tokens["access_token"]
    }

    data={
        "template_object": json.dumps({
            "object_type": "text",
            "text": content,
            "link": {
                "web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!",
                "mobile_web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!"
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)
