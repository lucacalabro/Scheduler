# emailsender("Soggetto email", "<h1>Titolo</h1><p>Paragrafo1</p><p>Paragrafo2</p>", [], ['luca.calabro@unimib.it', 'l.calabro2@campus.unimib.it'],['calabroluca78@gmail.com', 'lucalalabro78@live.com'])
# emailsender("Soggetto email", "<h1>Titolo</h1><p>Paragrafo1</p><p>Paragrafo2</p>", ['lucalalabro78@gmail.com'], ['luca.calabro@unimib.it', 'l.calabro2@campus.unimib.it'],['calabroluca78@gmail.com', 'lucalalabro78@live.com'])
def emailsender(subject, body, listTO, listCC, listBCC):
    # documentazione consultata
    # https://stackoverflow.com/questions/1546367/python-how-to-send-mail-with-to-cc-and-bcc
    # https://docs.python.org/3/library/email.examples.html
    import smtplib

    # Import the email modules we'll need
    from email.message import EmailMessage

    msg = EmailMessage()
    msg.add_header('Content-Type', 'text/html')

    email_content = f"<html><head></head><body>{body}</body></html>"
    msg.set_payload(email_content)
    # msg.set_content(email_content)

    msg['Subject'] = subject
    # msg['From'] = "serviziwebsi@unimib.it"
    msg['From'] = "noreplay@unimib.it"
    msg['To'] = ', '.join(listTO)
    msg['Cc'] = ', '.join(listCC)
    msg['Bcc'] = ', '.join(listBCC)

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.ehlo()  # protocollo per extended SMTP
    s.starttls()
    s.login("serviziwebsi@unimib.it", "?sciliam*15")
    s.send_message(msg)
    s.quit()