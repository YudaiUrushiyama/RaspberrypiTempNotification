#参考URL：https://note.com/klayer123/n/nb14086840351

import json
import requests

#Tokenの文字列取得
f = open ('SwitchbotToken.txt')    
Switchbot_token = f.readline()
print(Switchbot_token)
f.close ( )

# Please get your access token via switchbot app
header = {"Authorization": Switchbot_token}

# Get all device information in your switchbot hub
response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)

# Get switchbot bot "deviceId" in all device information
#if部分を取得したい温湿度計(Meter)に変更
bots_id  = [device["deviceId"] for device in devices['body']['deviceList'] if "Meter" == device["deviceType"]]

print(bots_id)

# Get all switchbot bot power state and output on your display

#for bot_id in bots_id:
 
#response = requests.get("https://api.switch-bot.com/v1.0/devices/" + bot_id + "/status", headers=header)
#bot      = json.loads(response.text)
#power    = bot['body']['power']

#print("bot id (" + bot_id + ") power : " + power)

