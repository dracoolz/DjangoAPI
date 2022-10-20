## Running the Application

Create the DB tables first:
```
python manage.py migrate
```
Run the development web server:
```
python manage.py runserver 8080
```
Open the URL http://localhost:8080/ to access the application.

How it works? Using [Postman](https://www.postman.com/downloads/).
Router for url will be look like this :
1. POST
   - /users : Create a new Tutorial

2. GET
   -  /users : Retrieve all Tutorials
   -  /users/:id : Retrieve a single Tutorial by id
   -  /users?title=res : Find all Tutorials which title contains ‘res’
   -  /users/published : Find all published Tutorials

3. PUT
   -  /users/:id Api: Update a Tutorial

4. DELETE
   -  /users/:id : Delete a Tutorial
   -  /users : Delete all Tutorials 
