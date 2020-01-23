"""Fee Calculator tests module."""
import json

import pytest

import app


@pytest.fixture
def client():
    """flask client fixture"""
    yield app.app.test_client()


def test_hello_world(client):
    """Test hello world."""
    rv = client.get("/")
    assert b"/fee/12/1500 > 70" in rv.data


def test_fee_calculator(client):
    """Test fee calculator."""
    rv = client.get("/fee/12/1500")
    data = json.loads(rv.data)
    assert len(data) == 3
    assert data["term"] == 12
    assert data["loan"] == 1500
    assert data["fee"] == 70
