# Tests for your routes go here


"""
When: we make a GET request to /albums
Then: we should get a list of all albums in the database
"""
def test_get_albums_returns_list_of_albums(web_client):
    assert False


"""
When: we make a POST request to /albums
And: we provide "Voyage" for `title`, "2022" for `release_year`, and "2" for `artist_id`
Then: we should get a 200 response with no content,
    and the new album should appear in the list when we make a GET request to /albums
"""
def test_post_albums_adds_new_album_to_list(web_client):
    assert False