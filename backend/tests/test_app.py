from app import app

def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b"Welcome" in res.data

def test_metrics():
    client = app.test_client()
    res = client.get('/metrics')
    assert res.status_code == 200

