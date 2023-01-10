from telegram import __version__ as TG_VER
import annas_archive as anna
import re
import urllib3
import MemePy

from telegram import ForceReply, Update

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    await update.message.reply_html(
        rf"Oi {user.mention_html()}!, boyzera demais? Use o comando /pesquisar com o nome ou o ISBN de um livro que você quer baixar.",
        reply_markup=ForceReply(
            selective=True, input_field_placeholder='/pesquisar '),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Uai, quer ajuda com o quê?!")


async def search_book(update: Update, context) -> None:
    name = " ".join(context.args)
    books = anna.search(name, limit=3)
    if (len(books) == 0):
        await update.message.reply_text('Não encontrei nenhum livro')
    else:
        suggestions = ""
        for book in books:
            if (len(books) > 1):
                suggestions = suggestions + \
                    book[1][:50]+", de "+book[0][:50]+". "+book[4]+"\n"

            else:
                suggestions = book[1]+", de "+book[0]+". "+book[3]+"\n"
        suggestions = "Oi! Essas são minhas sugestões:\n"+suggestions
        await update.message.reply_text(suggestions)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    MemePy.MemeGenerator.save_meme_to_disk(
        'Classy', 'memes', ["Bibliotecaria virtual", update.message.text])
    await update.message.reply_document(document=open('memes/meme.jpg', 'rb'))
    await update.message.reply_text("tô anotando tudo, meus advogados entrarão em contato!")
    print(update.message.text)


def main() -> None:
    api_key = open('../telegram_api_key.token', 'r').readline().strip('\n')
    application = Application.builder().token(api_key).build()
    print('Rodando...')
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("pesquisar", search_book))

    application.add_handler(MessageHandler(filters.TEXT, echo))
    application.run_polling()


if __name__ == "__main__":

    main()
