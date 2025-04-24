from requests import get, post, put, delete, HTTPError


def test_api():
    """
    An automated version of the manual testing I've been doing,
    testing the lifecycle of an inserted document.
    """
    user_root = "http://localhost:8000/users/"

    initial_doc = {
        "username": "jdoe",
        "firstname": "John",
        "lastname": "Doe",
    }

    try:
        # Insert a user
        response = post(user_root, json=initial_doc)
        response.raise_for_status()
        doc = response.json()
        inserted_id = doc["id"]
        print(f"Inserted document with id: {inserted_id}")
        print(
            "If the test fails in the middle you may want to manually remove the document."
        )
        assert doc["username"] == "jdoe"
        assert doc["firstname"] == "John"
        assert doc["lastname"] == "Doe"

        # List users and ensure it's present
        response = get(user_root)
        response.raise_for_status()
        user_id = {s["id"] for s in response.json()["users"]}
        assert inserted_id in user_id

        # Get individual user doc
        response = get(user_root + inserted_id)
        response.raise_for_status()
        doc = response.json()
        assert doc["id"] == inserted_id
        assert doc["username"] == "jdoe"
        assert doc["firstname"] == "John"
        assert doc["lastname"] == "Doe"

        # Update the user doc
        response = put(
            user_root + inserted_id,
            json={
                "firstname": "Jane",
            },
        )
        response.raise_for_status()
        doc = response.json()
        assert doc["id"] == inserted_id
        assert doc["username"] == "jdoe"
        assert doc["firstname"] == "Jane"
        assert doc["lastname"] == "Doe"

        # Get the user doc and check for change
        response = get(user_root + inserted_id)
        response.raise_for_status()
        doc = response.json()
        assert doc["id"] == inserted_id
        assert doc["username"] == "jdoe"
        assert doc["firstname"] == "Jane"
        assert doc["lastname"] == "Doe"

        # Delete the doc
        response = delete(user_root + inserted_id)
        response.raise_for_status()

        # Get the doc and ensure it's been deleted
        response = get(user_root + inserted_id)
        assert response.status_code == 404
    except HTTPError as he:
        print(he.response.json())
        raise