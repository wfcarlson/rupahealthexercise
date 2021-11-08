## Email Service REST API

### Requirements:
[Install Docker](https://docs.docker.com/get-docker/)
[Install docker-compose](https://docs.docker.com/compose/install/)

### To Run and test:

Create an .env file in the root of the project directory like:

```
SECRET_KEY=secretkey
EMAIL_PROVIDER=mailgun
#EMAIL_PROVIDER=sendgrid
SENDGRID_API_KEY=sendgridapikey
MAILGUN_API_KEY=mailgunapikey
```

Add values for django secret key and sendgrid and mailgun api keys

then:


`docker-compose build`
`docker-compose up`

`curl -X POST -H 'Content-Type: application/json' -d '{ \
    "to": "fake@fake.com", \
    "to_name": "Mr. Fake", \
    "from": "no-reply@fake.com", \
    "from_name": "Ms. Fake", \
    "subject": "A message from The Fake Family", \
    "body": "<h1>Your Bill</h1><p>$10</p>" \
}'`


