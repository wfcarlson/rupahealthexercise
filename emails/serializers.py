from emails.models import Email
from rest_framework import serializers

from .models import Email

class EmailSerializer(serializers.ModelSerializer):
    to = serializers.EmailField()
    to_name = serializers.CharField(max_length=200)
    #from is python keyword
    vars()['from'] = serializers.EmailField()
    from_name = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=200)
    body = serializers.CharField(max_length=200)

    class Meta:
        model = Email
        fields = ('to', 'to_name', 'from', 'from_name', 'subject', 'body')