# Using httpie to Test the API

`httpie` is a user-friendly command-line HTTP client. If you don't have it installed, you can install it using uv:

```bash
uv tool install httpie
```

#### Create a User

```bash
http POST "http://127.0.0.1:8000/users/" username="jdoe" firstname="John" lastname="Doe"
```

#### List All Users

```bash
http GET "http://127.0.0.1:8000/users/"
```

#### Get a Specific User (replace `<user_id>` with the actual user ID)

```bash
http GET "http://127.0.0.1:8000/users/<user_id>"
```

#### Update a User (replace `<user_id>` with the actual user ID)

```bash
http PUT "http://127.0.0.1:8000/users/<user_id>" firstname="Jane"
```

#### Delete a User (replace `<user_id>` with the actual user ID)

```bash
http DELETE "http://127.0.0.1:8000/users/<user_id>"
```