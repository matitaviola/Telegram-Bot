import Constants as keys
from telegram.ext import *
import Bot_Response as BR
print("I'm ready")
def start_command(update, context):
    update.message.reply_text('Ask me something')

def help_command(update, context):
    update.message.reply_text('Try one of these : "who are you?", "who am i?", "what is my level"')

def handle_message(update, context):
    msg = str(update.message.text).lower()
    response = BR.sample_response(msg)

    update.message.reply_text(response)

def error_log(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    update = Updater(keys.API_KEY, use_context=True)
    dispatch = update.dispatcher
    dispatch.add_handler(CommandHandler("start", start_command))
    dispatch.add_handler(CommandHandler("help", help_command))
    dispatch.add_handler(MessageHandler(Filters.text, handle_message))
    dispatch.add_error_handler(error_log)

    update.start_polling(0)#il numero tra parentesi è ogni quanti secondi aspetta prima di verificare se ci sono nuovi messaggi
    update.idle()

main()