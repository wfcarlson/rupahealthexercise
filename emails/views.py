from django.contrib.auth.models import User, Group
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import html2text

from .serializers import EmailSerializer
from .models import Email
from .services import email_service

h = html2text.HTML2Text()
h.ignore_links = False

class EmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = Email(**serializer.data)
            
            #convert html to plain text
            email.body = h.handle(email.body)

            response = email_service.send_email(email)
            print(response.status_code)
            print(response.text)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

"""
{
"from":"walterc@vt.edu",
"to":"walterc@vt.edu",
"to_name":"Walter C.",
"from_name":"Also Walter C.",
"subject":"test email",
"body":"<h1>title</h1><p>test email</p>"
}
"""