from flask import flash, render_template


def test_home_page_redirects_to_book_list(client):
    response = client.get("/")

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/books")


def test_health_check_reports_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_base_layout_shows_navigation(app):
    with app.test_request_context():
        html = render_template("base.html")

    assert "Library Borrowing System" in html
    assert 'href="/books"' in html
    assert 'href="/members"' in html
    assert 'href="/loans/overdue"' in html


def test_base_layout_shows_flashed_messages(app):
    with app.test_request_context():
        flash("No copies available", "error")
        html = render_template("base.html")

    assert "No copies available" in html
