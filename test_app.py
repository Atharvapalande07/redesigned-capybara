import app

def test_hello_world():
    response = app.app.test_client().get("/hello")
    assert response.status_code == 200
    assert response.data == b'Hello World'


def test_goodbye():
    response = app.app.test_client().get('/Goodbye')
    assert response.status_code == 404
