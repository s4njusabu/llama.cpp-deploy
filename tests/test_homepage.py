from fastapi.testclient import TestClient
from llamacpp_deploy import main, config

client = TestClient(main.app)


def test_homepage():

    assert client.get("/").status_code == 200
