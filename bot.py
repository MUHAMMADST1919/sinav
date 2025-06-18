from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# توکن ربات خود را اینجا قرار دهید
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update: Update, context: CallbackContext) -> None:
    """ارسال پیام خوش‌آمدگویی وقتی کاربر دستور /start را می‌فرستد"""
    user = update.effective_user
    update.message.reply_text(f"سلام {user.first_name}!\nبه ربات من خوش آمدید!")

def help_command(update: Update, context: CallbackContext) -> None:
    """ارسال پیام راهنما وقتی کاربر دستور /help را می‌فرستد"""
    update.message.reply_text("""
    دستورات موجود:
    /start - شروع کار با ربات
    /help - نمایش این راهنما
    """)

def echo(update: Update, context: CallbackContext) -> None:
    """تکرار پیام کاربر"""
    update.message.reply_text(update.message.text)

def main() -> None:
    """شروع ربات"""
    # ایجاد Updater و ارسال توکن
    updater = Updater(TOKEN)

    # دریافت dispatcher برای ثبت handlerها
    dispatcher = updater.dispatcher

    # ثبت handlerها برای دستورات مختلف
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # ثبت handler برای تکرار پیام‌های معمولی
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # شروع ربات
    updater.start_polling()

    # اجرای ربات تا زمانی که کاربر Ctrl+C را فشار دهد
    updater.idle()

if __name__ == '__main__':
    main()