# mini-tweeter

##### This documentation explain how to use mini-tweeter application

* 👉🏼 to run server, go to the root repository:
```bash
uvicorn main:app
```
* List of API endpoint:

| Endpoint | feature |
| ------ | ------ |
| post /users | user create |
| post /users/signup | sign up user |
| get /api/users | User list |
| put /users/{user_id} | modify user |
| delete /users/{user_id}| delete user |
| get /home| Home page |
| post /users/tweet | create tweet |
| get /users/tweet| tweet List |
| put /users/tweet/{tweet_id}| modify tweet |
| delete /users/tweet/{tweet_id}| Delete tweet  |

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/users' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "test",
  "password": "testpassword",
  "email": "test@gmail.com"
}'
````

