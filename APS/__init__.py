# from .mailer import emailsender
#
# emailsender("Soggetto email", "<h1>Titolo</h1><p>Paragrafo1</p><p>Paragrafo2</p>", ['lucalalabro78@gmail.com'], ['luca.calabro@unimib.it', 'l.calabro2@campus.unimib.it'],['calabroluca78@gmail.com', 'lucalalabro78@live.com'])
from .scheduler import start

start()