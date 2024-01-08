import requests
import datetime
API_KEY='8e03d0147ae7359a6d95926dbd5eca96'
APP_ID="0a57b8cf"
END_POINT='https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_end='https://api.sheety.co/272d5a45db0be49eb0b256d1f75d8139/myWorkouts/workouts'
header={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}
params={
    "query":input('What do you do?')
}
response = requests.request("POST", END_POINT,json=params,headers=header)
print(response.json()['exercises'][0]['duration_min'])
sheety_params={
    "workout":{
        "date":str(datetime.datetime.now().strftime("%d/%m/%Y")),
        "time":str(datetime.datetime.now().strftime("%H:%M")),
        "exercise":response.json()['exercises'][0]['name'].title(),
        "duration":response.json()['exercises'][0]['duration_min'],
        "calories":response.json()['exercises'][0]['nf_calories']
    }
}
header_sheety ={
    "Authorization": "Basic WWFuU2hhc2hrb3U6MDkwMzE5NzNXaWZp"
}
response_sheety = requests.request("POST",sheety_end,json=sheety_params,headers=header_sheety)
print(response_sheety.json())