# https://apscheduler.readthedocs.io/en/latest/index.html
# https://medium.com/@kevin.michael.horan/scheduling-tasks-in-django-with-the-advanced-python-scheduler-663f17e868e6
# python manage.py runserver - -noreload
# paragrafo "VI. Putting it all together"

from apscheduler.schedulers.background import BackgroundScheduler
from .mailer import emailsender


# E' un job da eseguire(deve essere senza parametri)
def send_email():
    # qui va inserita tutta la logica per stabilire quando l'email deve
    # essere inviata (accesso al model)
    subject = "Email schedulata"
    body = "<h1>Email schedulata</h1><p>Email schedulata</p>"
    listTO = ['luca.calabro@unimib.it']
    listCC = []
    listBCC = []
    emailsender(subject,
                body,
                listTO,
                listCC,
                listBCC)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'interval', minutes=1)
    scheduler.start()


def get_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'interval', minutes=1)
    return scheduler
