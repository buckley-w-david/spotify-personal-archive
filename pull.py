from bs4 import BeautifulSoup
import toml
from urllib.request import urlopen
from urllib.parse import urljoin

SPOTIFY_PREFIX='https://open.spotify.com'
config = toml.load("config.toml")

print(f"# My Playlists")
for playlist in config["Playlists"]:
    playlist_url = urljoin(urljoin(SPOTIFY_PREFIX, '/playlist/'), playlist['id'])
    with urlopen(playlist_url) as request:
        soup = BeautifulSoup(request.read(), features="html.parser")

    print(f"# {playlist['name']}")
    for track in soup.find_all(class_='tracklist-col name'):
        *artists, album = track.find_all('a')
        artist_entries = []

        for artist in artists:
            artist_url = urljoin(SPOTIFY_PREFIX, artist.get('href'))
            artist_entry = f"[{artist.text}]({artist_url})"
            artist_entries.append(artist_entry)

        album_url = urljoin(SPOTIFY_PREFIX, album.get('href'))
        album_entry = f"[{album.text}]({album_url})"

        song_entry = track.find('span').text
        print(f" - {song_entry} from {album_entry} by {', '.join(artist_entries)}")
