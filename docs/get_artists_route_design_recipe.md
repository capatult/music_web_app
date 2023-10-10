# GET /artists Route Design Recipe

## 1. Route Signature

```
# EXAMPLE

# List all artists route
GET /artists
```

## 2. Examples for testing

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# GET /artists
# Example expected response after seeding (200 OK):
"""\
[Artists(1, Pixies, Rock), ..., Artists(4, Nina Simone, Jazz)]\
"""
```

## 3. Test-drive the Route

```python
"""
GET /artists
  Expected response (200 OK):
  "[Artists(1, Pixies, Rock), ..., Artists(4, Nina Simone, Jazz)]"
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode(UTF_8) == "[Artists(1, Pixies, Rock), ..., Artists(4, Nina Simone, Jazz)]"

```
