#参考URL:https://knt60345blog.com/line-notify/

#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#LineTokenの文字列取得
f = open ('LineToken.txt')    
line_token = f.readline()
#print(line_token)
f.close ( )

#改行コードを削除してトークン格納
line_notify_token = line_token[:-1]
line_notify_api = 'https://notify-api.line.me/api/notify'

# メイン関数
def main():
    send_line_message('テストメッセージ')

# LINEへメッセージを送信する関数
def send_line_message(notification_message):

    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f' {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == "__main__":
    main()
