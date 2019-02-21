#pip install python-telegram-bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import GetPanel
import GetPanel
import sys

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def validate_group(bot, update):
    ''' '''
    #-30880111: Selected group
    if not abs(bot.get_chat(update.message.chat_id).id + 30880111):
      return True
    return False

def start(bot, update):
    """Send a message when the command /start is issued."""
    if not validate_group(bot, update):
        update.message.reply_text('Not allowed.')
        return
    #print(bot.get_chat(update.message.chat_id).id)
    update.message.reply_text('Hello there! Ready to show some Data.')

def help(bot, update):
    if not validate_group(bot, update):
        return
    """Send a message when the command /help is issued."""
    update.message.reply_text('Type /getG to get grafana graph status.')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

# Get an image from /tmp and sent to telegram bot
def getG(bot, update, args):
    """ """
    if not validate_group(bot, update):
        return
    chat_id=update.message.chat_id
    ResultGraf=GetPanel.GetGrafanaImage()
    if not ResultGraf:
       bot.send_photo(chat_id=chat_id, photo=open('/tmp/grafchart.png', 'rb'))
    #bot.send_message(chat_id=update.message.chat_id, text=args[0])
    else:
       bot.send_message(chat_id=update.message.chat_id, text="Unknow error.") 
    
def echo(bot, update):
    """Echo the user message."""
    #update.message.reply_text(update.message.text)
    pass
def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("681692264:AAFxxxxxxxxxxxx")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
        # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler("viewg", viewg, pass_args=True))
   
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
if __name__ == '__main__':
    main()