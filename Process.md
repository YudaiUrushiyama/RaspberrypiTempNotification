# Process
ここで行った手順の記録を残す

## 1.通知部分作成
ラズパイから自分のLINEに通知が来るように作成
LINEトークン発行
参考URL:https://knt60345blog.com/line-notify/

## 2.Switchbot温湿度計からの情報取得部分作成
Switchbotのトークン発行
Apiより、デバイスIDをもとに温度、湿度の取得
参考URL:https://note.com/klayer123/n/nb14086840351

## 3.Main.pyで温湿度をLINEに通知

## 4.ラズパイで実行確認
sshでラズパイに転送
コマンド：scp -r 送信元フォルダ 送信先フォルダ（ラズパイ）

