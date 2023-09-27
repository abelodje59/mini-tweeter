import os
from typing import Iterator
import asyncio

import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer


from core.config import settings
from main import app
from typing import Generator

DB_URL = "sqlite://:memory:"


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def client() -> Generator:
    initializer(
        db_url=settings.SQLITE_URL,
        modules={"models": [settings.TORTOISE_MODELS]}
    )

    with TestClient(app) as test_client:
        yield test_client

    finalizer()