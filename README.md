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
   ![image](https://user-images.githubusercontent.com/82569123/197674215-33be95c8-f40c-4966-9ebe-6076eebd0cae.png)


2. GET
   -  api/users : Retrieve all users
   ![image](https://user-images.githubusercontent.com/82569123/197674327-22ff5c1c-0b4b-4852-ab22-420ccd8fd8c5.png)

   -  api/users/:id : Retrieve a single user by id
   ![image](https://user-images.githubusercontent.com/82569123/197674400-2249fe13-d5af-425c-8b2b-784e89ba7b41.png)
   
   
3. PUT
   -  api/users/:id Api: Update a user
   1. 
   ![image](https://user-images.githubusercontent.com/82569123/197674893-a05f80a4-2124-4a1a-8444-8f06634ea0d4.png)
   2. 
   ![image](https://user-images.githubusercontent.com/82569123/197674999-465a3ad1-d555-484d-a539-6b047b21f479.png)


4. DELETE
   -  api/users/:id : Delete a user
   1. 
   ![image](https://user-images.githubusercontent.com/82569123/197675157-372e8727-e3af-44ca-b50d-98ef74fcc4a8.png)
   2. 
   ![image](https://user-images.githubusercontent.com/82569123/197675262-f604466b-135b-4ba8-b66b-06d1b92de172.png)

   -  api/users : Delete all users 
   1. 
   ![image](https://user-images.githubusercontent.com/82569123/197675339-9b16e9c1-965c-47ea-b4c0-43af20ac64ce.png)
   2. 
   ![image](https://user-images.githubusercontent.com/82569123/197675396-26062cda-fac3-4880-8f44-a87e03d8b72d.png)
