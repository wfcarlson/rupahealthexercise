from django.db import models

class Email(models.Model):

    to = models.CharField(max_length=200)
    to_name = models.CharField(max_length=200)
    #from is python keyword
    vars()['from'] = models.CharField(max_length=200)
    from_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    
    def __str__(self):
        return f"To: {self.to}, From: {getattr(self,'from')}, Subject: {self.subject}"
