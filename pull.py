from bs4 import BeautifulSoup
import toml
from urllib.request import urlopen
from urllib.parse import urljoin

SPOTIFY_PREFIX='https://open.spotify.com'
config = toml.load("config.toml")

playlist_url = urljoin(urljoin(SPOTIFY_PREFIX, '/playlist/'), config['playlist'])
with urlopen(playlist_url) as request:
    soup = BeautifulSoup(request.read(), features="html.parser")

print(f"# {config['name']}")
for track in soup.find_all(class_='tracklist-col name'):
    *artists, song = track.find_all('a')
    artist_entries = []
    # import pdb; pdb.set_trace()

    for artist in artists:
        artist_url = urljoin(SPOTIFY_PREFIX, song.get('href'))
        artist_entry = f"[{artist.text}]({artist_url})"
        artist_entries.append(artist_entry)

    song_url = urljoin(SPOTIFY_PREFIX, song.get('href'))
    song_entry = f"[{song.text}]({song_url})"

    print(f" - {song_entry} - {', '.join(artist_entries)}")
