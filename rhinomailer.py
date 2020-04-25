import sys
from smtplib import SMTP

"""
To Make This Work Change The Mailserver, login, password and sender.
Alter the contents of the message  but keeep the formatting.
Use a list of extracted email addresses only (one on each line)
Name list of email addresses contacts.txt.
"""


port = 25
mail_server = "mail.example.com"
login = "username"
password = "password"
list_name = "contacts.txt"
list_count = 0
sent_count = 0
message = """Subject: My Mellow Is Not Yellow
To: {recipient}
From: {sender}
<img width="632" height="801" src="https://www.ryangeddes.com/wp-content/uploads/2020/04/Screenshot_1.jpg"
class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="self-signed generated SLL certificate
displayed white text on black background"
srcset="https://www.ryangeddes.com/wp-content/uploads/2020/04/Screenshot_1.jpg 632w,
https://www.ryangeddes.com/wp-content/uploads/2020/04/Screenshot_1-237x300.jpg 237w,
https://www.ryangeddes.com/wp-content/uploads/2020/04/Screenshot_1-395x500.jpg 395w" sizes="(max-width: 632px) 100vw, 632px">
<p>Below are the quick commands needed to get your <strong>SSL</strong> certificate and key.  If you are trying to
create a certificate for Web (<strong>https</strong>) you can take advantage of the free <em>signed</em> certificates
that <a href="https://cloudflare.com">Cloudflare</a> provides,. <strong>Self-signing a certificate for web use, paticularly e-commerce, is a bad idea</strong>,
its best to use Cloudflare or purchase a <a href="https://www.dnsrhino.com/products/ssl">reputable signed certificate</a>.
A <em>signed certificate</em> signifies a trusted authority issuued it.  This provides SEO benefits in addition to security.
Visitors to your site will get warnings if you try to us a self-signed certificate.  </p>
"""
sender = "Someone", "someone@somewhere.com"

f = open(list_name, 'r')
with SMTP(mail_server, port) as server:
    server.login(login, password)
    for email in f:
        server.sendmail(
            sender,
            email,
            message.format(recipient=email, sender=sender)
        )
        list_count += 1
        sys.stdout.write("Curently Sending Message: " + str(list_count) + " to " + (email))
        sys.stdout.flush()
sys.stdout.write("Send Complete")
