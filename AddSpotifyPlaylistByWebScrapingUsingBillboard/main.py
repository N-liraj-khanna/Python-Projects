import os
import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'

SPOTIFY_ENDPOINT = f'https://api.spotify.com/v1'

OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
USER_ID = os.environ['USER_ID']

headers = {
    "Authorization": f"Bearer {OAUTH_TOKEN}"
}

your_date = input("Billboard's date? (YYYY-MM-DD) ")

billboard_response = requests.get(url=BILLBOARD_URL + your_date)
billboard_response.raise_for_status()

soup = BeautifulSoup(billboard_response.text, 'html.parser')
list_of_songs = []
for song in soup.find_all(class_='chart-element__information__song'):
    list_of_songs.append(song.string)


create_playlist_params = {
    "name": f"Billboard Hot 100({your_date})",
    "description": "Spotify Playlist Using Web Scraping on BillBoard for a given Date",
    "public": False
}
create_playlist_response = requests.post(url=F'{SPOTIFY_ENDPOINT}/users/{USER_ID}/playlists',
                                         json=create_playlist_params, headers=headers)
create_playlist_response.raise_for_status()
playlist_json_data = create_playlist_response.json()
playlist_id = playlist_json_data['external_urls']['spotify'].split('/')[4]

# playlist_id = 'your_playlist_id'  # got it from the above code

for song in list_of_songs:
    search_song_param = {
        'q': song,
        'type': 'track',
        'limit': 1,
        'offset': 1
    }
    search_response = requests.get(url=f'{SPOTIFY_ENDPOINT}/search', params=search_song_param, headers=headers)
    track_url = search_response.json()['tracks']['items'][0]['uri']

    add_track_params = {
        'uris': track_url
    }

    add_tracks_response = requests.post(url=f'{SPOTIFY_ENDPOINT}/playlists/{playlist_id}/tracks'
                                        , headers=headers, params=add_track_params)
    add_tracks_response.raise_for_status()
