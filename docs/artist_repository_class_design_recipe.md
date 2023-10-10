# Table `artists` Model and Repository Classes Design Recipe

## 1. Design and create the Table

(Already done)

## 2. Create Test SQL seeds

(Already done)

## 3. Define the class names

```python
# Table name: artists

# Model class
# (in lib/artist.py)
class Artist

# Repository class
# (in lib/artist_repository.py)
class ArtistRepository

```

## 4. Model class

```python
# Table name: artists

# Model class
# (in lib/artist.py)

class Artist:
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    def __eq__(self, other):
        pass  # Test-drive this

    def __repr__(self):
        pass  # Test-drive this
```

## 5. Repository Class interface

```python
# Table name: artists

# Repository class
# (in lib/artist_repository.py)

class ArtistRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT * FROM artists;

        # Returns an array of Artist objects.

    def create(artist):
        # Executes the SQL query:
        # INSERT INTO artists (name, genre) VALUES (%s, %s); %s, %s are artist.name, artist.genre respectively

        # Returns None.

```

## 6. Test Examples

```python
# Repo 1
# Get all students

repo = ArtistRepository()

artists = repo.all()

artists == [
Artist(1, 'Pixies', 'Rock'),
Artist(2, 'ABBA', 'Pop'),
Artist(3, 'Taylor Swift', 'Pop'),
Artist(4, 'Nina Simone', 'Jazz'),
]  # => True

# Repo 2
# Add an artist

repo = Artist()

new_artist = Artist(None, 'Wild nothing', 'Indie')

repo.create(new_artist)  # Returns nothing but adds row to end of seeded table corresponding to Artist(5, Wild nothing, Indie)

# Model: 5 standard tests:
#   - Can create
#   - Values assigned correctly upon creation
#   - Identical models compare equal
#   - Non-identical models compare nonequal
#   - Model formats into a string correctly
```


## 7. Test-drive and implement the Repository class behaviour
