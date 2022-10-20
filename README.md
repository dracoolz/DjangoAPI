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
   - api/users : Create a new Tutorial

2. GET
   -  api/users : Retrieve all Tutorials
   -  api/users/:id : Retrieve a single Tutorial by id
   -  api/users?title=res : Find all Tutorials which title contains ‘res’
   -  api/users/published : Find all published Tutorials

3. PUT
   -  api/users/:id Api: Update a Tutorial

4. DELETE
   -  api/users/:id : Delete a Tutorial
   -  api/users : Delete all Tutorials 
