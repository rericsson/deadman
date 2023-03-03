import pytest
from flask.testing import FlaskClient
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_service(client: FlaskClient):
    resp = client.post(
        "/service", json={"email_address": "some@thing.com", "username": "mehdi"}
    )

    assert resp.status_code == 200
    assert resp.json.get("success")


def test_service_bad_http_method(client: FlaskClient):
    """should return a Method Not Allowed response"""
    resp = client.get("/service")
    assert resp.status_code == 405


def test_service_no_json_body(client: FlaskClient):
    """should return a Bad Request response"""
    resp = client.post("/service", data="something")
    assert resp.status_code == 400
    assert not resp.json.get("success")


def test_service_missing_email(client: FlaskClient):
    """should return a Bad Request response"""
    resp = client.post("/service", json={"username": "mehdi"})
    assert resp.status_code == 400
    assert not resp.json.get("success")
