from fastapi.testclient import TestClient

from llamacpp_deploy import main

client = TestClient(main.app)


def test_homepage():

    assert client.get("/").status_code == 200
