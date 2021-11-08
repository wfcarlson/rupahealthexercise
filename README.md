## Email Service REST API

### Requirements:
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install docker-compose](https://docs.docker.com/compose/install/)

### To Run and test:

- Create an .env file in the root of the project directory like:

```
SECRET_KEY=secretkey
EMAIL_PROVIDER=mailgun
#EMAIL_PROVIDER=sendgrid
SENDGRID_API_KEY=sendgridapikey
MAILGUN_API_KEY=mailgunapikey
```

- Add values for django secret key and sendgrid and mailgun api keys
then:


- `docker-compose build`
- `docker-compose up`

- `curl -X POST localhost:8000/email -H 'Content-Type: application/json' -d '{ "to": "fake@fake.com", "to_name": "Mr. Fake", "from": "no-reply@fake.com", "from_name": "Ms. Fake", "subject": "A message from The Fake Family", "body": "<h1>Your Bill</h1><p>$10</p>"}'`

### Configuring:
To change between email providers simply edit the .env file, changing the EMAIL_PROVIDER value from `mailgun` to `sendgrid` and restart the docker-compose service

## Technologies:
I chose to use docker-compose and Docker to make it very easy to build and run the application on different systems without having to worry about differences in machines, OS's or software versions. 

I chose python and Django for several reasons. I am already very comfortable with python and Django and they are in the job description and so I wanted to show competence using these technologies. Additionally, Django is very easy to set up and get started for a small project like this. I like a lot of the built in features it has that make Django quick to develop in. For example, the built-in admin console and the automatic reloading of source code in dev mode.

I chose to use django restframework because it provides a ton of functionality that makes it very easy to create a REST API. This framework also allows you to write your API's in an object oriented way and keeps the code very simple and readable.

The other packages I used I chose because they provided a specific functionality I did not want to have to implement myself, like requests to handle the API calls and html2text for converting html to plaintext.

## Tradeoffs:
The main tradeoff I made is that the code is overengineered for the relatively simple task of POSTing requests to two email providers. I did this mainly so the solution would be easily extensible. If this had been a real application, in the future we would surely want to add more endpoints beyond a single POST endpoint and more functionality in general. I also designed it in a way that more email providers could be added easily, by creating a class that inherits from the EmailProvider class and editing EmailService to include the new provider.
## Future work:
I spent about 3.5 hours on this exercise. If were to spend more time on these are some things I would improve:

- I have not added much documentation or Unit in the code. This would obviously improve the code quality by making it easier to read and understand and detect and debug any issues.

- "from" is a python keyword so I used a work-around (which seems a little hacky to me) to add it as an attribute to the model and serializer classes. It would probably be better to implement a solution without this hack, by using the attribute name "sender" in the code and linking "from" in the REST body to "sender" in the serializer and model explicitly.

- Adding better error handling and logging. There is no logging to speak of really, and if the Email API's do not return a success code the REST call will fail silently instead of returning the error to the user. 

- Extending the code to support other Email providers. I tried to implement the code in a way that would be easily extensible more providers.