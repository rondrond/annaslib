from mastodon import Mastodon
from mastodon import StreamListener
import annas_archive as anna
import re

botat = '@bibliotecaria'
hashtag ="pfv"
thanks = "brigad"

mastodon = Mastodon(access_token = '../token.secret', api_base_url = 'https://botsin.space/')

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

class Listener(StreamListener):
    def on_notification(self, notification):
        if(notification["type"] == "mention"):
            book_name = remove_html_tags(notification["status"]["content"]).lower().replace(botat, '')
        
            if(len(notification["status"]["tags"])>0):
                clean_tags = []
                for tag in notification["status"]["tags"]:
                    clean_tags.append(tag["name"].lower())
                    book_name = book_name.replace(tag["name"], '')
                book_name = book_name.replace('#', '')

                if(hashtag in clean_tags):    
                    print(f'Nova menção de @{notification["account"]["acct"]}, pedindo {book_name}\n')
                    books = anna.search(book_name, limit=3)
                    suggestions = ""
                    for book in books:
                        suggestions = suggestions + book[1][:50]+", de "+book[0][:50]+". "+book[4]+"\n"
                    suggestions = "@"+notification["account"]["acct"]+" Oi! Essas são minhas sugestões:\n"+suggestions
                    mastodon.status_post(suggestions, in_reply_to_id=notification["status"]["id"], visibility='direct')
                    print(suggestions)

            elif(book_name.__contains__(thanks)):
                msg = "@"+notification["account"]["acct"]+" eu que agradeço, flor!"
                mastodon.status_post(msg, in_reply_to_id=notification["status"]["id"], visibility='direct')
                print(f'Agradeci a {notification["account"]["acct"]}')

            mastodon.notifications_dismiss(notification["id"])

mastodon.stream_user(Listener())