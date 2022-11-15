import sendgrid
import os
from sendgrid.helpers.mail import*
sg=sendgrid.SendGridAPIClient(api_key='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')
from_email=Email("navnoble910@gmail.com")
to_email=To("navinsashaang020@gmail.com")
subject="sendgrid integration"
content=Content("text/plain", "welcome aboard your registration was successful")
mail=Mail(from_email,to_email,subject,content)
response=sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
    
