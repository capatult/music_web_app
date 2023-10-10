# POST /artists Route Design Recipe

## 1. Route Signature

```
# Create a new artist route
POST /artists
```

## 2. Examples for testing

```python
# POST /artists
# Expected response after seeding (200 OK):
""
```

## 3. Test-drive the Route

```python
"""
POST /artists
  Expected response (200 OK):
  \"\"
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response_1 = web_client.post('/artists',
        data={"name": "Wild nothing", "genre": "Indie"})
    assert response_1.status_code == 200
    assert response_2.data.decode(UTF_8) == ""
    
    response_2 = web_client.get('/artists')
    assert response_2.status_code == 200
    assert response_2.data.decode(UTF_8) == "[Artist(1, Pixies, Rock), ..., Artist(5, Wild nothing, Indie)]"

```
