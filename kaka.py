from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace 'your_token_here' with your actual bot token
Token = "7053898252:AAF8mVh1uykdsh8JHpZmRo7JF3KtGpgCLrU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Welcome to Kaka.ai')

async def holo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('hello this is pokki')

async def Shojol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('se akta madarcud')

async def shornok(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('or thka vlo sele r hoy na')

async def Sifat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('khala lover')

async def shovon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('sele vlo kinto aktu matal ')

async def Fayaz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('anika er jamai ')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
        /help -> ami meeting e asi pore knock koro
    """)

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Tmr nani re chudii')

# Create the Application and pass it your bot's token.
application = Application.builder().token(Token).build()

# Add command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('content', content))
application.add_handler(CommandHandler('Shojol', Shojol))
application.add_handler(CommandHandler('Sifat', Sifat))
application.add_handler(CommandHandler('shovon', shovon))
application.add_handler(CommandHandler('shornok', shornok))
application.add_handler(CommandHandler('sakib', holo))
application.add_handler(CommandHandler('Fayaz', Fayaz))

# Run the bot until the user presses Ctrl-C
application.run_polling()
