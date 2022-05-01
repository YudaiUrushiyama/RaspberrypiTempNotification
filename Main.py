#

#from re import L
import Switchbot_temp
import LINE_Notification
import json

#実行
def main():
    humid,temp = Temp_Get()
    Line(humid,temp)


def Temp_Get():
    #Switchbotの温湿度計よりstate取得
    resp = Switchbot_temp.Switchbot_Temp_get()
    
    #print(resp.text)   #debugprint

    bot               = json.loads(resp.text)
    deviceId          = bot['body']['deviceId']
    humidity:float    = bot['body']['humidity']
    temperature:float = bot['body']['temperature']

    #debug print
    #print("deviceId    : " + deviceId )
    #print("humidity    : " , humidity )
    #print("temperature : " , temperature )

    return humidity,temperature

def Line(humid:float,temp:float):

    text = "湿度は {0} で、温度は {1} です。"
    send_text = text.format(humid,temp)
    LINE_Notification.send_line_message(send_text)


if __name__ == "__main__":
    main()

