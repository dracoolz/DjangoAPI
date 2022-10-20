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
   - api/users : Create a new User

2. GET
   -  api/users : Retrieve all users
   -  api/users/:id : Retrieve a single user by id
   -  api/users?title=res : Find all user which title contains ‘res’
   -  api/users/published : Find all published users

3. PUT
   -  api/users/:id Api: Update a user

4. DELETE
   -  api/users/:id : Delete a user
   -  api/users : Delete all users 
