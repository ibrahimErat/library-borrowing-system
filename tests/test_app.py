def test_home_page_shows_product_name(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Library Borrowing System" in response.data


def test_health_check_reports_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
