

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='navnoble910@gmail.com',
    to_emails='navnoble910@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e
    )