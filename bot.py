from mastodon import Mastodon
from mastodon import StreamListener
import annas_archive as anna
import re
botat = '@bibliotecaria'

mastodon = Mastodon(
    access_token = '../token.secret',
    api_base_url = 'https://botsin.space/'
)
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

class Listener(StreamListener):
        def on_notification(self, notification):
            book_name = remove_html_tags(notification["status"]["content"]).replace(botat, '')
            if((notification["type"] == "mention") and (len(book_name)<30)):
                print(f'Nova menção de @{notification["account"]["acct"]}, pedindo {book_name}\n')
                books = anna.search(book_name, limit=3)
                print(f'Livro solicitado: {book_name}, minhas sugestões são:')
                suggestions = ""
                for book in books:
                    suggestions = suggestions + book[1][:50]+", de "+book[0][:50]+". "+book[4]+"\n"
                suggestions = "@"+notification["account"]["acct"]+" Oi! Essas são minhas sugestões:\n"+suggestions
                mastodon.status_post(suggestions, in_reply_to_id=notification["status"]["id"])
                print(suggestions)
                
#            elif((notification["type"] == follow)):
#                print(f'Pedido de seguir de {notification["account"]["acct"]}, seguindo de volta!')
#                mastodon.follows(notification["account"]["acct"])
            
            mastodon.notifications_dismiss(notification["id"])

mastodon.stream_user(Listener())