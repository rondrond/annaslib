from telegram import __version__ as TG_VER
import annas_archive as anna
import MemePy

from telegram import ForceReply, Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    await update.message.reply_html(
        rf"Oi {user.mention_html()}!, boyzera demais? Tudo que você digitar será pesquisado. Não é preciso usar nenhum comando. Agora também mostro mais resultados! Os outros comandos são /ajuda e /start, pra iniciar o bot.",
        reply_markup=ForceReply(
            selective=True, input_field_placeholder='/pesquisar '),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Uai, quer ajuda com o quê?! Ainda não posso te ajudar em nada. Apenas digite o nome do livro ou ISBN que ele será pesquisado")


async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Uai, quer ajuda com o quê?!")


async def search_book(update: Update, context) -> None:
    name = update.message.text
    books = anna.search(name, limit=6)
    if len(books) == 0:
        await update.message.reply_text('Não encontrei nenhum livro')
    else:
        suggestions = ""
        for book in books:
            if len(books) > 1:
                suggestions = suggestions + \
                    book[1][:50]+", de "+book[0][:50] + \
                    " ("+book[2]+"). "+book[4]+"\n\n"

            else:
                suggestions = book[1]+", de "+book[0] + \
                    " ("+book[2]+"). "+book[3]+"\n"
        suggestions = "Oi! Essas são minhas sugestões:\n"+suggestions
        await update.message.reply_text(suggestions)


def main() -> None:
    api_key = open('../telegram_api_key.token', 'r').readline().strip('\n')
    application = Application.builder().token(api_key).build()
    print('Rodando...')
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", help_command))
    application.add_handler(CommandHandler("log", log_command))

    application.add_handler(MessageHandler(filters.TEXT, search_book))
    application.run_polling()


if __name__ == "__main__":

    main()
