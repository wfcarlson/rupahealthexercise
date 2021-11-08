import requests
import json
from abc import ABC, abstractmethod
from django.conf import settings

from .models import Email

class EmailService():

    def __init__(self):
        if settings.EMAIL_PROVIDER == 'mailgun':
            self.provider = MailgunEmailProvider()
        elif settings.EMAIL_PROVIDER == 'sendgrid':
            self.provider = SendgridEmailProvider()

    def send_email(self, email: Email):
        return self.provider.send_email(email)

class EmailProvider(ABC):

    def send_email(self, email: Email):
        auth = self.get_auth()
        headers = self.get_headers()
        request_body = self.get_request_body(email)

        return requests.post(
                settings.EMAIL_PROVIDER_URL,
                headers=headers,
                auth=auth,
                data=request_body)

    @abstractmethod
    def get_request_body(self, email: Email):
        raise NotImplementedError()

    @abstractmethod
    def get_headers(self):
        raise NotImplementedError()

    @abstractmethod
    def get_auth(self):
        raise NotImplementedError()

class SendgridEmailProvider(EmailProvider):

    def get_request_body(self, email: Email):
        
        return json.dumps({
            "personalizations": [{"to": [{"email": email.to, "name": email.to_name}]}],
            "from": {"email": vars(email)['from'], "name": email.from_name},
            "subject": email.subject,
            "content": [{"type": "text/plain", "value": email.body}]
        })

    def get_headers(self):
        return {
            "Authorization": "Bearer " + settings.EMAIL_PROVIDER_API_KEY,
            "Content-Type": "application/json"
        }

    def get_auth(self):
        return None

class MailgunEmailProvider(EmailProvider):

    def get_request_body(self, email: Email):
        return {
            "from": f"{email.from_name} <{vars(email)['from']}>",
            "to": [f"{email.to_name} <{email.to}>"],
            "subject": email.subject,
            "text": email.body
        }

    def get_headers(self):

        return {}

    def get_auth(self):

        return ("api", settings.EMAIL_PROVIDER_API_KEY)

email_service = EmailService()