import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return str(
        repository.all()
    )

@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.create(Album(
        id=None,
        title=request.form['title'],
        release_year=request.form['release_year'],
        artist_id=request.form['artist_id']
    ))
    return ""


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

