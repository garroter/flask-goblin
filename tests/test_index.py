import pytest


@pytest.mark.usefixtures("client")
class TestIndex:
    def test_view(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert b"Example" in response.data
