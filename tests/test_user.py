from fastapi.testclient import TestClient
import asyncio

from models.twitter import User


async def create_user():
    user = await User.create(
        username="Odolab",
        password="Odolab59",
        email="Odolab59@gmail.com"
    )

    return user


def test_create_user(client: TestClient,
                        event_loop: asyncio.AbstractEventLoop) -> None:

    article = event_loop.run_until_complete(create_user())

    response = client.get("/api/users")
    assert response.status_code == 200
    content = response.json()
    first_user = content[0]
    assert first_user["username"] == article.username
    assert first_user["password"] == article.password
    assert first_user["email"] == article.email

