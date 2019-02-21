### Simple Grafana Telegrambot Example

Simple example of grafana alerting to telegram and telegram bot command.


### Introduction
**Clone repository:**
https://github.com/jporven/simple-grafana-telegrambot-example

Start Influxdb and Grafana
```bash
cd grafana
docker-compose up -d
```
**Create database**
```bash
curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE testdb"
```
Add values to the database
```bash
sh grafana/generate.sh
```
**Create a telegram bot**
Search for @BotFather
/newbot
Chose a name and username
Ej:
GrafanaAlerting
grafanaalerting_bot
BotFather bot show the URL to access the bot and access token.

https://t.me/Grafanaalerting_bot

Token example:
token:
  732375761:AAGNBmRWGDyIZb-i9evBbZ1N9JJqNoNxjdE
name:
  GrafanaAlerting
username:
  @Grafanaalerting_bot

For grafana integration we also need a bot ID.

The URL allows to get messages updates including other metadata information
https://api.telegram.org/bot<YourBOTToken>/getUpdates

Send a dummy mensaje to a bot
example: /start
Get updates
Example URL:
```bash
 curl https://api.telegram.org/bot732375761:AAGNBmRWGDyIZb-i9evBbZ1N9JJqNoNxjdE/getUpdates
```
Example of curl response:
```json
"message":{"message_id":9,"from":{"id":592642742,"is_bot":false,"first_name":"Joe-Bel","language_code":"en"},
"chat":{"id":592642742,"first_name":"Joe-Bel","type":"private"},"date":1550747829,"text":"/help","entities":[{"offset":0,"length":5,"type":"bot_command"}]}}]}
```

Get bot ID
In this case:
  "id":592642742

To get a telegram group ID the procedure is the same. Adding a bot to a group and excecute an URL call. The negative ID is asociated to a group. The group ID is used to allow access to a telegram bot only for group members. This restrictions need to be programmend using the telemgram bot API.

####Grafana configuration

**Create an alert in grafana**
[Grafana alert creation](doc/gif/grafana_create_alert.gif?raw=true "Grafana alert creation")

With a telegram bot created grafana can be configured to send notification selecting a telegram channel.
**Configure telegram notification channel in grafana**
[grafana notification channel whith telegram](doc/gif/grafana_telegram_send_notification.gif)

**Linking alerts trigered with a notification channel**

#####Telegram Bot command example to get a Grafana Pannel graph.

GetPanel.py: is a simple example that use a grafana api to get an image pannel and save it in a tmp location.
MonBot.py: Take /tmp/ saved image and send to a telegram bot with the programmed bot command.

**Issues**
Persisting grafana data: 
Set permissions to grafana volume to 472 in order to allow write
```bash
sudo chown 472:472 grafana/data/grafana
```


References
1. https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
2. https://github.com/python-telegram-bot/python-telegram-bot
   
