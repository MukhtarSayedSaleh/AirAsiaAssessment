# AirAsia coding assessment
### Muktar Sayed Saleh's solution


##### 1. The tech stack:
For this assesment and to keep it simple I've used the following architecture:
- [Django] and [Django Rest Framework]: For backend APIs, with one simple model (models.py -> Package model).
- [Swagger]: Documentation for the backend APIs.
- [jQuery] & [html5] frontend UI: simple enough for this assessemnt purposes.
- [Docker] containers: for easier deployment and development environment.
- [Docker Compose] confiugration: to set up the whole environment at once, easier for the tester to check my solution out.
- [MarkDown]: Used to write this documentation.


##### 2. How can you run my solution?
it is pretty straight forward to run the solution:

- Make sure you have docker installed, and then run the following commands:
```sh
$ cd <my_solutions_folder>
$ docker-compose up --build
```

###### How to test it after running it?

- now the backend service should be running on port 8000 (you can verify that by opening `http://localhost:8000/swagger`)
- and the frondend server should be working on the port 4200, so to test you can simple open your browser and navigate to `http://localhost:4200`.

[![Test](https://monjz-production.s3.me-south-1.amazonaws.com/airasia.gif)](https://monjz-production.s3.me-south-1.amazonaws.com/airasia.gif)


##### 3. Import Notes:
- I've written simple test cases to cover all the backend API endpoints which you can run via the following commands:
```sh
$ cd <my_solutions_folder>/backend
$ python manage.py test
```


Thank you & Happy coding!




   [Django]: <https://www.djangoproject.com>
   [Django Rest Framework]: <https://www.django-rest-framework.org>
   [Swagger]: <https://swagger.io>
   [Docker]: <https://www.docker.com>
   [Docker Compose]: <https://docs.docker.com/compose>
   [jQuery]: <http://jquery.com>
   [html5]: <https://www.w3schools.com/html/html5_intro.asp>
   [MarkDown]: <https://en.wikipedia.org/wiki/Markdown>