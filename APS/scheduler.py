# https://apscheduler.readthedocs.io/en/latest/index.html
# https://medium.com/@kevin.michael.horan/scheduling-tasks-in-django-with-the-advanced-python-scheduler-663f17e868e6
# python manage.py runserver - -noreload
# paragrafo "VI. Putting it all together"

from apscheduler.schedulers.background import BackgroundScheduler
from .mailer import emailsender


# E' un job da eseguire(deve essere senza parametri)
def send_email():
    #qui va inserita tutta la logica per stabilire quando l'email deve
    #essere inviata (accesso al model)
    subject = "Email schedulata"
    body = "<h1>Titolo</h1><p>Paragrafo1</p><p>Paragrafo2</p>"
    listTO = ['lucalalabro78@gmail.com', 'sergiosean.minelli@unimib.it']
    listCC = ['luca.calabro@unimib.it', 'l.calabro2@campus.unimib.it']
    listBCC = ['calabroluca78@gmail.com', 'lucalalabro78@live.com']
    emailsender(subject,
                body,
                listTO,
                listCC,
                listBCC)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'interval', minutes=1)
    scheduler.start()

