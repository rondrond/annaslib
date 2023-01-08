from mastodon import Mastodon
from mastodon import StreamListener
from bs4 import BeautifulSoup
import annas_archive as anna

botat = '@bibliotecaria'

mastodon = Mastodon(
    access_token = '../token.secret',
    api_base_url = 'https://botsin.space/'
)

class Listener(StreamListener):
        def on_notification(self, notification):
            if(notification["type"] == "mention"):
                book_name = BeautifulSoup(notification["status"]["content"], features="lxml").get_text().strip(botat)
                print(f'Nova menção de @{notification["account"]["acct"]}, pedindo {book_name}\n')
                books = anna.search(book_name, limit=3)
                print(f'Livro solicitado: {book_name}, minhas sugestões são:')
                suggestions = ""
                for book in books:
                    suggestions = suggestions + book[1][:50]+", de "+book[0][:50]+". "+book[4]+"\n"
                suggestions = "@"+notification["account"]["acct"]+" Oi! Essas são minhas sugestões:\n"+suggestions
                mastodon.status_post(suggestions, in_reply_to_id=notification["status"]["id"])
                print(suggestions)
                mastodon.notifications_dismiss(notification["id"])

mastodon.stream_user(Listener())