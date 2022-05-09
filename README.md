# RaspberrypiTempNotification

## 1. 作成物
ラズパイを使用して室内温度をLINEで通知する

## 2. 使用
 - Raspberrypi4
 - SwitchBot温湿度計

## 3.シーケンス
```mermaid
   sequenceDiagram
        autonumber
        participant ラズパイ
        participant Switchbot OpenAPI
        participant Switchbot温湿度計
        participant LINE Notify
        participant LINE User
        ラズパイ->>ラズパイ: Main.py実行
        ラズパイ->>Switchbot OpenAPI: APIへTokenをパラメーターにリクエスト
        Switchbot OpenAPI->>Switchbot温湿度計: 各種ステータス取得
        Switchbot温湿度計->>Switchbot OpenAPI: 各種ステータス
        Switchbot OpenAPI->>ラズパイ: 各種ステータス
        ラズパイ->>ラズパイ: 温度、湿度のみに加工&送信文字列作成

        ラズパイ->>LINE Notify: LINE NotifyへTokenと送信文字列をパラメーターにリクエスト
        LINE Notify->>LINE User: 送信文字列がUserへ送信


```

##
