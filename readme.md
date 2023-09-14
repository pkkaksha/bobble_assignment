
## BobbleAI Assignment

### Problem Statement

Fetch and Update Room temperatures

  Your task is to determine the following:

1. Post temp from a room.
2. Fetch all room temperatures.

### What to Expect

a. GET API - http://127.0.0.1:8000/sensors/fetch_temp/

b. POST API - http://127.0.0.1:8000/sensors/send_temp/

### How to Run the Solution

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver
4. To send temp from a particular room :
  a. Make a Post Call with data from POST_API mentioned above :

  {
    "room_id":2,
    "temp_in_room":30
  }

5. Fetch data from all room using GET_API url
